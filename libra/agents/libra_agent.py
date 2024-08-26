from libra.models import ModelFactory, ModelBackend
from libra.types import ModelLabel
from typing import List, Optional, Dict, Tuple
from libra.functions.retrieval_functions import RETRIEVAL_FUNCS
from colorama import Fore
from libra.functions import OpenAIFunction
from libra.config import ChatGPTConfig
from libra.prompts import (
    SYSTEM_INIT_PROMPT,
    LLAMAINDEX_REACT_PROMPT,
    TOOL_FORMAT_PROMPT
)

from libra.messages import OpenAIMessage
from libra.types import ChatCompletionChunk
from openai import Stream
from libra.utils import streaming as st
import libra.logs as logs


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


class LibraAgent:
    
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
                model_label=ModelLabel.GPT_4o,
                model_config_dict=ChatGPTConfig(
                    stream=True,
                    temperature=0.0
                ).__dict__
            )
        )                
        
        self.tools = (
            tools
            if tools is not None
            else RETRIEVAL_FUNCS
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
        messages: List[OpenAIMessage], # type: ignore
        window_size: int = 4
    ) -> Stream[ChatCompletionChunk]: # type: ignore
        prompts: List[OpenAIMessage] = [ # type: ignore
            {"role": "system", "content": self.system_message}
        ]
        limit = 2 * window_size + 1
        last_messages = messages[-limit:] if len(messages) > limit else messages
        prompts.extend(last_messages)
        
        logs.print_color(last_messages[-1], Fore.YELLOW)
        
        response = self.model.run(messages=prompts)
        
        stream_config = st.parse_stream(response)
        
        processed_text = st.join_content_of(stream_config['processed'])
        
        if stream_config['answer'] != st.Ans.ONE:
            logs.print_color(processed_text, Fore.LIGHTCYAN_EX)
            
        if stream_config['action']:
            name = stream_config['action']['name']
            arguments = stream_config['action']['args']
            results = self.tool_dict[name](**arguments)
            logs.print_color(results, Fore.BLUE)
            prompts.extend([
                {"role": "assistant", "content": processed_text},
                {"role": "user", "content": f"Observation:  {results}"}
            ])
            
            second_response = self.model.run(prompts) # type: ignore
            second_stream_config = st.parse_stream(second_response)            
            for chunk in st.get_stream_from(
                response=second_response, 
                config=second_stream_config
            ):
                if st.is_valid(chunk):
                    yield chunk # type: ignore
        else:
            generator = st.get_stream_from(
                response=response,
                config=stream_config
            )
            
            for chunk in generator:
                yield chunk # type: ignore                           
        

if __name__ == "__main__":
    import time
    
    agent = LibraAgent()
    
    response = agent.step(messages=[
        {"role": "user", "content": "MB có bao nhiêu công ty con?"},
    ])    
      
    for chunk in response:        
        logs.print_color(st.content_of(chunk), Fore.LIGHTGREEN_EX, end="")
    print()
  