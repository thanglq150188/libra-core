from libra.types import ChatCompletionChunk
from openai import Stream
from typing import Dict, List, Tuple
from enum import Enum
import json


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


def first_chunk_of(
    response: Stream[ChatCompletionChunk] # type: ignore
) -> ChatCompletionChunk: # type: ignore    
    first_chunk = response.__next__()
    while not is_valid(first_chunk):
        first_chunk = response.__next__()
    return first_chunk


def tokens_from(text: str) -> List[str]: # type: ignore
    tokens = text.split(' ')
    output_tokens = []
    for token in tokens:
        output_tokens.append(token)
        output_tokens.append(' ')
    output_tokens = output_tokens[:-1]
    return output_tokens


import time
import tiktoken
from openai.types.chat.chat_completion_chunk import Choice, ChoiceDelta


def fake_chat_completion_stream(text: str, model: str = "gpt-4o") -> Stream[ChatCompletionChunk]: # type: ignore
    # Initialize the tokenizer
    enc = tiktoken.encoding_for_model(model)
    
    # Tokenize the text
    tokens = enc.encode(text)
    
    # Simulate streaming by yielding chunks of tokens
    for i, token in enumerate(tokens):
        chunk = ChatCompletionChunk(
            id=f"chatcmpl-{i}",
            object="chat.completion.chunk",
            created=1677652288 + i,  # Fake timestamp
            model=model,
            choices=[
                Choice(
                    index=0,
                    delta=ChoiceDelta(content=enc.decode([token])),
                    finish_reason=None
                )
            ]
        )
        time.sleep(0.01)
        yield chunk # type: ignore
    
    # Yield the final chunk to indicate completion
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
    ) # type: ignore


ERROR_MSG = "Xin lỗi bạn nha, hiện tại mình đang gặp trục trặc kỹ thuật nên chưa thể trả lời câu hỏi này. Bạn vui lòng hỏi câu khác hoặc quay lại sau nhé? Cảm ơn bạn đã thông cảm!"


class Verbal(Enum):
    THOUGHT = "thought"
    ANSWER = "answer"
    ACTION = "action"
    PARAMS = "params"
    TEXT = "text"
    
    
def verbal_of(chunk: ChatCompletionChunk) -> Verbal: # type: ignore
    chunk_content = content_of(chunk).lower()
    if chunk_content == "thought":
        return Verbal.THOUGHT
    if chunk_content == "answer":
        return Verbal.ANSWER
    if chunk_content == "action":
        return Verbal.ACTION
    if chunk_content == "params":
        return Verbal.PARAMS
    return Verbal.TEXT
    
    
class AgentResponse:
    
    def __init__(
        self, 
        source: Stream[ChatCompletionChunk] # type: ignore
    ) -> None:
        self.source = source
        self.flag = Verbal.TEXT
        self.component = {
            Verbal.TEXT: "",
            Verbal.ANSWER: "",
            Verbal.THOUGHT: "",
            Verbal.ACTION: "",
            Verbal.PARAMS: ""
        }
        
    def action(self) -> str:
        return self.component[Verbal.ACTION]
    
    def params(self) -> str:
        return self.component[Verbal.PARAMS]
        
        
    def reset_component(self):
        self.component = {chunk_type: "" for chunk_type in Verbal}
        
    def stream(self) -> Stream[ChatCompletionChunk]: # type: ignore
        first_token = True
        self.reset_component()
        for chunk in self.source:
            verbal = verbal_of(chunk)
            if verbal != Verbal.TEXT:
                self.source.__next__()
                self.flag = verbal
                first_token = True
            else:
                if first_token:
                    set_content(chunk, content_of(chunk).strip())
                    first_token = False

                self.component[self.flag] += content_of(chunk)
                if self.flag in [Verbal.TEXT, Verbal.ANSWER]:
                    time.sleep(0.01)
                    if is_valid(chunk):
                        yield chunk # type: ignore
        
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
                for chunk in fake_chat_completion_stream(ERROR_MSG):
                    yield chunk # type: ignore
                    
    def to_action_msg(self):
        return f"""Thought: {self.component[Verbal.THOUGHT]}
Action: {self.component[Verbal.ACTION]}
Params: {self.component[Verbal.PARAMS]}
"""
        

if __name__ == "__main__":

    # Example usage
    text = """
Thought: The current language of the user is Vietnamese. I need to use a tool to help me answer the question. Then I need to extract the input to chosen tool.
Action: hihihaha
Params: {"query": "taij sao lai"}
"""

    agent_response = AgentResponse(fake_chat_completion_stream(text))
    for chunk in agent_response.stream():
        pass
    # print()
    print(agent_response.to_action_msg())
    
    