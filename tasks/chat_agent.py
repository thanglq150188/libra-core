from libra.models import ModelFactory, ModelBackend
from libra.types import ModelLabel, ChatCompletion, ChatCompletionChunk
from typing import List, Optional, Dict, Union
from openai import Stream
from libra.functions.retrieval_functions import (
    RETRIEVAL_FUNCS,
    mb_information_retrieval,
    job_retrieval
)

from libra.functions import OpenAIFunction
from libra.config import ChatGPTConfig
from libra.prompts import SYSTEM_INIT_PROMPT
from libra.messages import OpenAIMessage


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
        messages: List[OpenAIMessage]
    ): # type: ignore
        
        prompts: List[OpenAIMessage] = [
            {"role": "system", "content": self.system_message}
        ]
        prompts.extend(messages)
        
        response = self.model.run(messages=messages)
        
        # parsing to see if there is a tool call
        first_chunk = response.__next__()
        tool_call_first_chunk = first_chunk.choices[0].delta.tool_calls
        if tool_call_first_chunk is not None:
            # tool call not None, there is a tool use case
            tool_id = tool_call_first_chunk.id
            tool_name = tool_call_first_chunk.function.name
            tool_arguments = tool_call_first_chunk.function.arguments
            for chunk in response:
                tool_call_chunk = chunk.choices[0].delta.tool_calls[0] 
                tool_arguments += tool_call_chunk.function.arguments
        else:
            # not tool use, just return normal chunk
            yield chunk.json() # type: ignore
        
if __name__=="__main__":
    chat_agent = ChatAgent()
    