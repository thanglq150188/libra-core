from libra.models import ModelFactory, ModelBackend
from libra.types import ModelLabel
from typing import List, Optional, Dict, Tuple
from libra.functions.libra_functions import LIBRA_FUNCS
from colorama import Fore
from libra.functions import OpenAIFunction
from libra.config import ChatGPTConfig
from libra.prompts import (
    SYSTEM_INIT_PROMPT,
    LLAMAINDEX_REACT_PROMPT,
    TOOL_FORMAT_PROMPT
)

import json

from libra.messages import OpenAIMessage
from libra.types import ChatCompletionChunk
from openai import Stream
import libra.logs as logs
import libra.response.streams as st

from dotenv import load_dotenv

load_dotenv(override=True)


def create_libra_system_prompt(
    inner_system_message: str,
    tools: List[OpenAIFunction]
) -> str:
    tools_desc = []

    for func in tools:
        tool_desc = TOOL_FORMAT_PROMPT.format(
            tool_name = func.get_function_name(),
            tool_description = func.get_function_description(),
            tool_argument = func.get_openai_tool_schema()['function']['parameters'],
        )
        tools_desc.append(tool_desc)                
    tool_names = [func.get_function_name() for func in tools]
    
    prompt = LLAMAINDEX_REACT_PROMPT.format(
        tool_desc = '\n'.join(tools_desc),
        tool_names = ', '.join(tool_names),
        context_prompt = inner_system_message
    )
    
    return prompt


import os

class LibraAgent:
    
    def __init__(
        self,
        system_message: Optional[str] = None,
        model: Optional[ModelBackend] = None,
        tools: Optional[List[OpenAIFunction]] = None,
    ) -> None:
        
        model_label = ModelLabel.AZURE_GPT_4o if os.environ['MODEL_USE'] =='AZURE' else ModelLabel.GPT_4o
        
        self.model: ModelBackend = (
            model
            if model is not None
            else ModelFactory.create(
                model_label=model_label,
                model_config_dict=ChatGPTConfig(
                    stream=True,
                    temperature=0.0
                ).__dict__
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
    
    def step(
        self,
        messages: List[OpenAIMessage],
        window_size: int = 4
    ) -> Stream[ChatCompletionChunk]: # type: ignore
        prompts: List[OpenAIMessage] = [ # type: ignore
            {"role": "system", "content": self.system_message}
        ]
        limit = 2 * window_size + 1
        last_messages = messages[-limit:] if len(messages) > limit else messages
        prompts.extend(last_messages)
        
        logs.print_color(f"Question: {last_messages[-1]['content']}", Fore.YELLOW) # type: ignore
        
        response = self.model.run(messages=prompts)
        
        aresponse = st.AgentResponse(response)
        for chunk in aresponse.stream():
            logs.print_color(st.content_of(chunk), Fore.LIGHTGREEN_EX, end="")
            yield chunk # type: ignore
            
        action = aresponse.action()        
        if action != "":
            params = json.loads(aresponse.params())
            observation = self.tool_dict[action](**params)
            logs.print_color(aresponse.to_action_msg(), Fore.LIGHTCYAN_EX)
            logs.print_color(observation, Fore.BLUE)
            prompts.extend([
                {"role": "assistant", "content": aresponse.to_action_msg()},
                {"role": "user", "content": f"Observation: {observation}"}
            ])
            response_2nd = self.model.run(prompts) # type: ignore
            aresponse_2nd = st.AgentResponse(response_2nd)
            for chunk in aresponse_2nd.stream():
                logs.print_color(st.content_of(chunk), Fore.LIGHTGREEN_EX, end="")
                yield chunk # type: ignore
            

if __name__=="__main__":
    import time
    
    agent = LibraAgent()
    
    response = agent.step(messages=[
        {"role": "user", "content": "Tôi đang học chuyên ngành Tài chính Ngân hàng. Tôi có thể làm việc ở những vị trí gì?"},
    ])
    
    for chunk in response:
        pass