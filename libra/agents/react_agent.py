from libra.models import ModelFactory, ModelBackend
from libra.types import ModelLabel
from typing import List, Optional, Dict, Union
from libra.functions.libra_functions import (
    LIBRA_FUNCS
)

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
import json
import tiktoken


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


def check_valid(chunk: ChatCompletionChunk) -> bool: # type: ignore
    if chunk.choices is not None:
        if len(chunk.choices) > 0:
            if chunk.choices[0].delta is not None:
                if chunk.choices[0].delta.content is not None:
                    if chunk.choices[0].delta.content != "":
                        return True
    return False


def get_content(chunk: ChatCompletionChunk) -> str: # type: ignore
    return chunk.choices[0].delta.content


def get_first_chunk(
    response: Stream[ChatCompletionChunk] # type: ignore
) -> ChatCompletionChunk: # type: ignore    
    first_chunk = response.__next__()
    while not check_valid(first_chunk):
        first_chunk = response.__next__()
    return first_chunk


def convert_string_to_tokens(text: str) -> List[str]: # type: ignore
    tokens = text.split(' ')
    output_tokens = []
    for token in tokens:
        output_tokens.append(token)
        output_tokens.append(' ')
    output_tokens = output_tokens[:-1]
    return output_tokens


def parse_streaming_response(
    response: Stream[ChatCompletionChunk] # type: ignore
) -> Dict: # type: ignore
    text_response = ""
    
    first_chunk = get_first_chunk(response)
    first_chunk_content = get_content(first_chunk)
    if (first_chunk_content != "Thought") and (first_chunk_content != "thought"):
        return {
            "Error": None,
            "answer": True,
            "action": None,
            "prototype": None
        }
    
    text_response += first_chunk_content
    
    for chunk in response:
        if check_valid(chunk):
            chunk_content = get_content(chunk)
            if (chunk_content == "Answer") or (chunk_content == "answer"):
                response.__next__() # remove ':' sign
                return {
                    "Error": None,
                    "answer": True,
                    "action": None,
                    "prototype": None
                }
            text_response += chunk_content
    
    import json

    lines = text_response.split("\n")
    for line in lines:
        if line.startswith("Action: "):
            action = line.replace("Action: ", "")
        if line.startswith("Action Input: "):
            action_input = line.replace("Action Input: ", "")
            try:
                action_input = json.loads(action_input)
            except json.JSONDecodeError:                
                return {
                    "Error": "Mình hiện tại chưa thể trả lời câu hỏi này của bạn do lỗi hệ thống, bạn vui lòng hỏi câu khác nha",
                    "answer": False,
                    "action": None,
                    "prototype": first_chunk.copy()
                }
    
    return {
        "Error": None,
        "answer": False,
        "action": {'name': action, 'args': action_input},
        "response": text_response,
        "prototype": None
    }
    

class ReactAgent:
    
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
        prompts: List[OpenAIMessage] = [
            {"role": "system", "content": self.system_message}
        ]
        limit = 2 * window_size + 1
        last_messages = messages[-limit:] if len(messages) > limit else messages
        prompts.extend(last_messages)
        
        response = self.model.run(messages=prompts)        
        
        parsed_params = parse_streaming_response(response)        
        
        if parsed_params['Error'] is not None:
            error_msg = str(parsed_params['Error'])
            for token in convert_string_to_tokens(error_msg):
                chunk = parsed_params['prototype'].copy()
                chunk.choices[0].delta.content = token
                yield chunk # type: ignore
        
        if parsed_params['answer']:
            if parsed_params['prototype'] is not None:
                yield parsed_params['prototype'] # type: ignore                
            for chunk in response:
                if check_valid(chunk):
                    yield chunk # type: ignore
                    
        if parsed_params['action'] is not None:
            name = parsed_params['action']['name']
            arguments = parsed_params['action']['args']
            response_text = parsed_params['response']
            results = self.tool_dict[name](**arguments)
            prompts.extend([
                {"role": "assistant", "content": response_text},
                {"role": "user", "content": f"Observation:  tài liệu được tìm thấy: {results} \nNote: Nếu tài liệu không có thông tin cần thiết, cứ trả lời là bạn không có đủ thông tin nên không thể giải đáp."}
            ])
            
            response = self.model.run(prompts) # type: ignore

            for chunk in response:
                if get_content(chunk) is not None:
                    yield chunk # type: ignore
    

if __name__ == "__main__":
    agent = ReactAgent()
    
    response = agent.step(messages=[
        {"role": "user", "content": "MB có hỗ trợ mua nhà không ?"},
    ])
    
    for chunk in response:
        print(get_content(chunk), end="")