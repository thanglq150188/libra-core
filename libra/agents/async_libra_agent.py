from libra.models import ModelFactory, ModelBackend
from libra.types import ModelLabel
from typing import List, Optional, Dict, Tuple, AsyncGenerator
from libra.functions.libra_functions import LIBRA_FUNCS
from colorama import Fore
from libra.functions import OpenAIFunction
from libra.config import ChatGPTConfig
import asyncio
from libra.prompts import (
    SYSTEM_INIT_PROMPT,
    LLAMAINDEX_REACT_PROMPT,
    TOOL_FORMAT_PROMPT,
    SYSTEM_ANSWER_PROMPT
)

import json

from libra.messages import OpenAIMessage
from libra.types import ChatCompletionChunk
from openai import AsyncStream
import libra.logs as logs
import libra.response.async_streams as st
from libra.config import (
    CHATGPT_CONFIG,
    COMMON_CONFIG
)

from dotenv import load_dotenv

load_dotenv(override=True)

import sys

def set_event_loop_policy():
    if sys.platform.startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    elif sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
        asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
    else:
        print(f"Unsupported platform: {sys.platform}")
        sys.exit(1)

set_event_loop_policy()


NOT_ENOUGH_DATA_MSG = "Xin lỗi bạn nha, hiện tại mình không có đủ dữ liệu để trả lời câu hỏi của bạn. Mình sẽ cập nhật thêm ở những phiên bản sau nhé"
EXCEPTION_MSG = "Xin lỗi bạn nha, hiện tại mình gặp một chút trục trặc nên không thể câu hỏi của bạn. Mình sẽ cập nhật sửa chữa thêm ở những phiên bản sau nhé"


def create_libra_system_prompt(
    inner_system_message: str,
    tools: List[OpenAIFunction]
) -> str:
    tools_desc = []

    def process_tool(func):
        tool_desc = TOOL_FORMAT_PROMPT.format(
            tool_name = func.get_function_name(),
            tool_description = func.get_function_description(),
            tool_argument = func.get_openai_tool_schema()['function']['parameters'],
        )
        return tool_desc

    tools_desc = [process_tool(func) for func in tools]
    tool_names = [func.get_function_name() for func in tools]
    
    prompt = LLAMAINDEX_REACT_PROMPT.format(
        tool_desc = '\n'.join(tools_desc),
        tool_names = ', '.join(tool_names),
        context_prompt = inner_system_message
    )
    
    return prompt


async def create_prompts(
    system_message, 
    conversation
) -> List[OpenAIMessage]: # type: ignore
    prompts: List[OpenAIMessage] = [ # type: ignore
        {"role": "system", "content": system_message}
    ]
    window_size = COMMON_CONFIG.window_size
    limit = 2 * window_size + 1
    last_messages = conversation[-limit:] if len(conversation) > limit else conversation
    prompts.extend(last_messages)
    return prompts


import os

class AsyncLibraAgent:
    
    def __init__(
        self,
        system_message: Optional[str] = None,
        model: Optional[ModelBackend] = None,
        tools: Optional[List[OpenAIFunction]] = None,
    ) -> None:
                
        self.model: ModelBackend = (
            model
            if model is not None
            else ModelFactory.create(
                model_label=COMMON_CONFIG.model,
                model_config_dict=CHATGPT_CONFIG.__dict__
            )
        )                
        
        self.tools = (
            tools
            if tools is not None
            else LIBRA_FUNCS
        )
        
        self.tool_dict = {
            tool.get_function_name(): tool.func for tool in self.tools
        }
        
        self.system_message = create_libra_system_prompt(
            tools=self.tools,
            inner_system_message= (
                system_message
                if system_message is not None
                else SYSTEM_INIT_PROMPT
            )
        )
        
    async def execute_tool(self, action: str, params: Dict) -> Dict:
        return await asyncio.to_thread(self.tool_dict[action], **params)
    
    async def astep(
        self,
        messages: List[OpenAIMessage], # type: ignore
    ) -> AsyncGenerator[ChatCompletionChunk, None]: # type: ignore
        try:
            prompts = await create_prompts(self.system_message, messages)
            
            logs.print_color(f"\nQuestion: {messages[-1]['content']}", Fore.YELLOW) # type: ignore

            action_count = 0
            previous_action = None
            stop = False
            while not stop:
                logs.print_color(f"\n>>>>>>>", color=Fore.BLUE) # type: ignore
                response = await self.model.run_async(messages=prompts)
                agent_response = st.AsyncAgentResponse(response) # type: ignore
                async for chunk in agent_response.astream():
                    yield chunk
                
                action = agent_response.action()
                if action != "":
                    stop = True
                    params = json.loads(agent_response.params())
                    tool_result = await self.execute_tool(action, params)
                    
                    logs.print_color('\n> ' + tool_result['display'], Fore.LIGHTBLUE_EX)                    

                    if action != previous_action:
                        action_count += 1
                    
                    prompts = await create_prompts(SYSTEM_ANSWER_PROMPT.format(document=tool_result['document']), messages)
                    response = await self.model.run_async(messages=prompts)
                    agent_response = st.AsyncAgentResponse(response) # type: ignore
                    async for chunk in agent_response.astream():
                        yield chunk # type: ignore
                else:
                    text = agent_response.text()
                    answer = agent_response.answer()
                    thought = agent_response.thought()
                    if text == "" and answer == "":
                        logs.print_color(f"\nNo answer found: {agent_response.to_action_msg()}", Fore.RED)
                        if thought != "":
                            async for chunk in st.fake_chat_completion_stream(thought):
                                logs.print_color(st.content_of(chunk), Fore.LIGHTGREEN_EX, end='')
                                yield chunk # type: ignore
                        else:
                            async for chunk in st.fake_chat_completion_stream(EXCEPTION_MSG):
                                logs.print_color(st.content_of(chunk), Fore.LIGHTGREEN_EX, end='')
                                yield chunk # type: ignore
        
                    stop = True
                
                previous_action = action
        except Exception as e:
            async for chunk in st.fake_chat_completion_stream(EXCEPTION_MSG):
                logs.print_color(st.content_of(chunk), Fore.LIGHTGREEN_EX, end='')
                yield chunk # type: ignore
            

async def main():
    agent = AsyncLibraAgent()
    
    async for chunk in agent.astep(messages=[
        {"role": "user", "content": "tôi giỏi văn, mà lại dốt toán, tôi nên theo hướng nghề nghiệp nào?"},
    ]):
        pass

if __name__=="__main__":
    asyncio.run(main())