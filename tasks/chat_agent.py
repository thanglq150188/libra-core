from libra.models import ModelFactory, ModelBackend
from libra.types import ModelLabel, ChatCompletion, ChatCompletionChunk
from typing import List, Optional, Dict, Union
from openai import Stream
from libra.functions.retrieval_functions import (
    RETRIEVAL_FUNCS,
    mb_information_retrieval,
    job_retrieval,
    mb_network_retrieval
)

from libra.functions import OpenAIFunction
from libra.config import ChatGPTConfig
from libra.prompts import SYSTEM_INIT_PROMPT
from libra.messages import OpenAIMessage
import json


class ChatAgent:
    
    def __init__(
        self,
        system_message: Optional[str] = None,
        model: Optional[ModelBackend] = None,
        tools: Optional[List[OpenAIFunction]] = None
    ) -> None:
        self.system_message:str = system_message if system_message is not None else SYSTEM_INIT_PROMPT
        self.model: ModelBackend = (
            model
            if model is not None
            else ModelFactory.create(
                model_label=ModelLabel.GPT_4o,
                model_config_dict=ChatGPTConfig(
                    tools=RETRIEVAL_FUNCS,
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
        
    def step(
        self, 
        messages: List[OpenAIMessage] # type: ignore
    ): # type: ignore
        
        prompts: List[OpenAIMessage] = [ # type: ignore
            {"role": "system", "content": self.system_message}
        ]
        prompts.extend(messages)
        
        response = self.model.run(messages=prompts)
        
        # parsing to see if there is a tool call
        first_chunk = response.__next__()
        tool_call_first_chunk = first_chunk.choices[0].delta.tool_calls
        if tool_call_first_chunk is not None:
            # tool call not None, there is a tool use case
            tool_id = tool_call_first_chunk[0].id
            tool_name = tool_call_first_chunk[0].function.name
            tool_arguments = tool_call_first_chunk[0].function.arguments
            for chunk in response:                
                finish_reason = chunk.choices[0].finish_reason
                if finish_reason is None:
                    tool_call_chunk = chunk.choices[0].delta.tool_calls[0] 
                    tool_arguments += tool_call_chunk.function.arguments
            tool_arguments = json.loads(tool_arguments)
            result = globals()[tool_name](**tool_arguments) # type: ignore
            tool_call_msg = {
                "role": "assistant",
                "tool_calls": [
                    {
                        "id": tool_id,
                        "type": "function",
                        "function": {
                            "name": tool_name,
                            "arguments": str(tool_arguments)
                        }
                    }
                ],    
            }
            
            # print(result)
            # Append the tool result to get the real answer
            prompts.extend([
                tool_call_msg,
                {"role":"tool", "tool_call_id": tool_id, "name": tool_name, "content":result} # type: ignore
            ])
            response = self.model.run(
                messages=prompts
            )
            
            for chunk in response:
                if len(chunk.choices) > 0:
                    chunk_text = chunk.choices[0].delta.content
                    if chunk_text is not None:
                        yield chunk
        else:
            # not tool use, just return normal chunk
            for chunk in response:
                if len(chunk.choices) > 0:
                    chunk_text = chunk.choices[0].delta.content
                    if chunk_text is not None:
                        yield chunk