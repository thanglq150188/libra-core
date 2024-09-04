import asyncio
from libra.types import ChatCompletionChunk
from openai import AsyncStream
from typing import Dict, List, Tuple, AsyncGenerator
from enum import Enum
import json
import time
import tiktoken
from openai.types.chat.chat_completion_chunk import Choice, ChoiceDelta
import libra.logs as logs
from colorama import Fore


def is_valid(chunk: ChatCompletionChunk) -> bool: # type: ignore
    if chunk.choices is not None:
        if len(chunk.choices) > 0:
            if chunk.choices[0].delta is not None:
                if chunk.choices[0].delta.content is not None:
                    if chunk.choices[0].delta.content != "":
                        return True
    return False


def set_content(chunk: ChatCompletionChunk, new_content:str): # type: ignore
    if is_valid(chunk):
        chunk.choices[0].delta.content = new_content
        

def trim(chunk: ChatCompletionChunk): # type: ignore
    if is_valid(chunk):
        text = content_of(chunk)
        set_content(chunk, text.strip())


def content_of(chunk: ChatCompletionChunk) -> str: # type: ignore
    if is_valid(chunk):
        return chunk.choices[0].delta.content
    return ""

def join_content_of(chunks: List[ChatCompletionChunk]) -> str: # type: ignore
    content = ""
    for chunk in chunks:
        content += content_of(chunk)
    return content

async def first_chunk_of(
    response: AsyncStream[ChatCompletionChunk] # type: ignore
) -> ChatCompletionChunk: # type: ignore
    async for chunk in response:
        if is_valid(chunk):
            return chunk
    raise StopAsyncIteration("No valid chunks found")

def tokens_from(text: str) -> List[str]: # type: ignore
    tokens = text.split(' ')
    output_tokens = []
    for token in tokens:
        output_tokens.append(token)
        output_tokens.append(' ')
    output_tokens = output_tokens[:-1]
    return output_tokens

async def fake_chat_completion_stream(
    text: str, 
    model: str = "gpt-4o"
) -> AsyncGenerator[ChatCompletionChunk, None]: # type: ignore
    enc = tiktoken.encoding_for_model(model)
    tokens = enc.encode(text)
    
    for i, token in enumerate(tokens):
        chunk = ChatCompletionChunk(
            id=f"chatcmpl-{i}",
            object="chat.completion.chunk",
            created=1677652288 + i,
            model=model,
            choices=[
                Choice(
                    index=0,
                    delta=ChoiceDelta(content=enc.decode([token])),
                    finish_reason=None
                )
            ]
        )
        await asyncio.sleep(0.01)
        yield chunk
    
    yield ChatCompletionChunk(
        id=f"chatcmpl-{len(tokens)}",
        object="chat.completion.chunk",
        created=1677652288 + len(tokens),
        model=model,
        choices=[
            Choice(
                index=0,
                delta=ChoiceDelta(),
                finish_reason="stop"
            )
        ]
    )

ERROR_MSG = "Xin lỗi bạn nha, hiện tại mình đang gặp trục trặc kỹ thuật nên chưa thể trả lời câu hỏi này. Bạn vui lòng hỏi câu khác hoặc quay lại sau nhé? Cảm ơn bạn đã thông cảm!"

class Verbal(Enum):
    THOUGHT = "THOUGHT"
    ANSWER = "ANSWER"
    ACTION = "ACTION"
    PARAMS = "PARAMS"
    TEXT = "TEXT"


def verbal_of(chunk: ChatCompletionChunk) -> Verbal: # type: ignore
    chunk_content = content_of(chunk)
    if chunk_content == "Thought":
        return Verbal.THOUGHT
    if chunk_content == "Answer":
        return Verbal.ANSWER
    if chunk_content == "Action":
        return Verbal.ACTION
    if chunk_content == "Params":
        return Verbal.PARAMS
    return Verbal.TEXT


def print_logs(text, flag: Verbal):
    if flag == Verbal.TEXT:
        logs.print_color(text, color=Fore.LIGHTGREEN_EX, end="")
    if flag == Verbal.ACTION:
        logs.print_color(text, color=Fore.LIGHTCYAN_EX, end="")
    if flag == Verbal.PARAMS:
        logs.print_color(text, color=Fore.CYAN, end="")
    if flag == Verbal.THOUGHT:
        logs.print_color(text, color=Fore.LIGHTCYAN_EX, end="")
    if flag == Verbal.ANSWER:
        logs.print_color(text, color=Fore.LIGHTGREEN_EX, end="")


class AsyncAgentResponse:
    def __init__(
        self, 
        source: AsyncStream[ChatCompletionChunk] # type: ignore
    ) -> None:
        self.source = source
        self.flag = Verbal.TEXT
        self.component = {verbal: "" for verbal in Verbal}
    
    # Existing synchronous methods remain unchanged
    def action(self) -> str:
        return self.component[Verbal.ACTION]
    
    def params(self) -> str:
        return self.component[Verbal.PARAMS]
    
    def answer(self) -> str:
        return self.component[Verbal.ANSWER]
    
    def thought(self) -> str:
        return self.component[Verbal.THOUGHT]
    
    def text(self) -> str:
        return self.component[Verbal.TEXT]
    
    def reset_component(self):
        self.component = {chunk_type: "" for chunk_type in Verbal}
    
    async def astream(self) -> AsyncGenerator[ChatCompletionChunk, None]: # type: ignore
        first_token = True
        self.reset_component()
        async for chunk in self.source:
            verbal = verbal_of(chunk)
            if verbal != Verbal.TEXT:
                await self.source.__anext__() # remove ':' sign
                self.flag = verbal
                first_token = True
                print_logs(verbal.value + ": ", self.flag)
            else:
                if first_token:
                    set_content(chunk, content_of(chunk).strip())
                    first_token = False
                
                print_logs(content_of(chunk), self.flag)

                self.component[self.flag] += content_of(chunk)
                if self.flag in [Verbal.TEXT, Verbal.ANSWER]:
                    await asyncio.sleep(0.01)
                    if is_valid(chunk):
                        yield chunk
        
        self.component = {
            verbal: self.component[verbal].strip()
            for verbal in Verbal
        }
        
        if self.component[Verbal.PARAMS] != "":
            try:
                json.loads(self.component[Verbal.PARAMS])
            except json.JSONDecodeError:
                self.component[Verbal.ACTION] = ""
                self.component[Verbal.PARAMS] = ""
                async for chunk in fake_chat_completion_stream(ERROR_MSG):
                    print_logs(content_of(chunk), Verbal.TEXT)
                    yield chunk
    
    def to_action_msg(self):
        return f"""Thought: {self.component[Verbal.THOUGHT]}
Action: {self.component[Verbal.ACTION]}
Params: {self.component[Verbal.PARAMS]}
"""

async def main():
    text = """
cuộc sống có giống cuộc đời lắm thay
Thought: The current language of the user is Vietnamese. I need to use a tool to help me answer the question. Then I need to extract the input to chosen tool.
Action: hihihaha
Params: {"query": "taij sao lai"}
"""

    agent_response = AsyncAgentResponse(fake_chat_completion_stream(text)) # type: ignore
    async for chunk in agent_response.astream():
        pass
    print(agent_response.to_action_msg())

if __name__ == "__main__":
    asyncio.run(main())