from libra.types import ChatCompletionChunk
from openai import Stream
from typing import Dict, List
from enum import Enum

class Ans(Enum):
    ZERO = 0 # no answer
    ONE = 1 # raw text
    TWO = 2 # answer with Answer :
    


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


def parse_stream(
    response: Stream[ChatCompletionChunk] # type: ignore
) -> Dict: # type: ignore
    
    processed = []
    action = None
    error_msg = None
    
    def create_output(answer: Ans):
        return {
            "error": error_msg,
            "action": action,
            "processed": processed,
            "answer": answer
        }
    
    
    first_chunk = first_chunk_of(response)
    first_chunk_content = content_of(first_chunk)
    processed.append(first_chunk)
    if (first_chunk_content != "Thought") and (first_chunk_content != "thought"):
        return create_output(answer=Ans.ONE)
    
    
    for chunk in response:
        if is_valid(chunk):
            processed.append(chunk)
            chunk_content = content_of(chunk)
            if (chunk_content == "Answer") or (chunk_content == "answer"):
                processed.append(response.__next__()) # remove ':' sign
                return create_output(answer=Ans.TWO)            
    
    import json

    processed_text = join_content_of(processed)
    tool_name = None
    tool_args = None
    lines = processed_text.split("\n")
    for line in lines:
        if line.startswith("Action: "):
            tool_name = line.replace("Action: ", "")
        if line.startswith("Action Input: "):
            tool_args = line.replace("Action Input: ", "")
            try:
                tool_args = json.loads(tool_args)
            except json.JSONDecodeError:
                error_msg = "Mình hiện tại chưa thể trả lời câu hỏi này của bạn do lỗi hệ thống, bạn vui lòng hỏi câu khác nha"                
                return create_output(answer=Ans.ZERO)
    
    if tool_name is None or tool_args is None:
        error_msg = "Mình hiện tại chưa thể trả lời câu hỏi này của bạn do lỗi hệ thống, bạn vui lòng hỏi câu khác nha"        
        return create_output(answer=Ans.ZERO)
    
    action = {'name': tool_name, 'args': tool_args}    
    return create_output(answer=Ans.ZERO)
    

def get_stream_from(
    response: Stream[ChatCompletionChunk], # type: ignore
    config: Dict
) -> Stream[ChatCompletionChunk]: # type: ignore    
    
    if config['error'] is not None:
        first_chunk = config['processed'][0].copy()
        error_msg = str(config['Error'])
        for token in tokens_from(error_msg):
            chunk = first_chunk.copy()
            chunk.choices[0].delta.content = token
            yield chunk # type: ignore
                                
    elif config['answer'] == Ans.ONE:
        if len(config['processed']) > 0:
            for chunk in config['processed']:
                yield chunk # type: ignore                
        for chunk in response:
            if is_valid(chunk):
                yield chunk # type: ignore
                
    elif config['answer'] == Ans.TWO:
        first_chunk = response.__next__()
        trim(first_chunk)
        yield first_chunk # type: ignore
        for chunk in response:
            if is_valid(chunk):
                yield chunk # type: ignore                
    
    else:
        first_chunk = config['processed'][0].copy()
        error_msg = str(config['Error'])
        for token in tokens_from(error_msg):
            chunk = first_chunk.copy()
            chunk.choices[0].delta.content = token
            yield chunk # type: ignore