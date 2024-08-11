# Imports
import json
import requests
from collections.abc import Callable
from typing import Annotated as A, Literal as L

import openai

from libra.functions import OpenAIFunction

import os

from dotenv import load_dotenv

load_dotenv(override=True)

openai_client: openai.OpenAI = openai.OpenAI(api_key=os.environ['OPENAI_API_KEY'])


class StopException(Exception):
    """
    Stop Execution by raising this exception (Signal that the task is Finished).
    """


def finish(answer: str) -> None:
    """
    Answer the user's question and finish the conversation.

    Args:
        answer (str): The answer to the user's question.

    Returns:
        None: This function raises an exception to end the conversation.
    """
    raise StopException(answer)


def get_current_location() -> str:
    """
    Get the current location of the user.

    Args:
        None

    Returns:
        str: A JSON string containing the latitude and longitude of the user's location.
    """
    return json.dumps(requests.get("http://ip-api.com/json?fields=lat,lon").json())


def get_current_weather(
    latitude: float,
    longitude: float,
    temperature_unit: str,
) -> str:
    """
    Get the current weather for a given location.

    Args:
        latitude (float): The latitude of the location.
        longitude (float): The longitude of the location.
        temperature_unit (str): The unit for temperature measurement ('celsius' or 'fahrenheit').

    Returns:
        str: A JSON string containing the current weather information.
    """
    resp = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": latitude,
            "longitude": longitude,
            "temperature_unit": temperature_unit,
            "current_weather": True,
        },
    )
    return json.dumps(resp.json())


def add(a: float, b: float) -> str:
    """
    Add two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        str: The result of the addition as a string.
    """
    return str(a + b)


def mul(a: float, b: float) -> str:
    """
    Multiply two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        str: The result of the multiplication as a string.
    """
    return str(a * b)


# All functions that can be called by the LLM Agent
name_to_function_map: dict[str, Callable] = {
    get_current_location.__name__: get_current_location,
    get_current_weather.__name__: get_current_weather,
    add.__name__: add,
    mul.__name__: mul,
    finish.__name__: finish,
}

# JSON Schemas for all functions
function_schemas = [
    OpenAIFunction(func).get_openai_tool_schema()
    for func in name_to_function_map.values()
]
    
    
QUESTION_PROMPT = "(344 + 5786) * 101 bằng mấy"
    
    
# Initial "chat" messages
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant who can answer multistep questions by sequentially calling functions. Follow a pattern of THOUGHT (reason step-by-step about which function to call next), ACTION (call a function to as a next step towards the final answer), OBSERVATION (output of the function). Reason step by step which actions to take to get to the answer. Only call functions with arguments coming verbatim from the user or the output of other functions. For calculations, use the 'add' and 'mul' functions instead of performing the calculations yourself.",
    },
    {
        "role": "user",
        "content": QUESTION_PROMPT,
    },
]


def run(messages: list[dict]) -> list[dict]:
    """
    Run the ReAct loop with OpenAI Function Calling.
    """
    # Run in loop
    max_iterations = 10
    for i in range(max_iterations):
        # Send list of messages to get next response
        response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=messages, # type: ignore
            tools=function_schemas, # type: ignore
            tool_choice="auto",
            stream=False
        )
        response_message = response.choices[0].message
        messages.append(response_message)  # type: ignore # Extend conversation with assistant's reply
        # Check if GPT wanted to call a function
        tool_calls = response_message.tool_calls
        if tool_calls:
            for tool_call in tool_calls:
                function_name = tool_call.function.name
                # Validate function name
                if function_name not in name_to_function_map:
                    print(f"Invalid function name: {function_name}")
                    messages.append(
                        {
                            "tool_call_id": tool_call.id,
                            "role": "tool",
                            "name": function_name,
                            "content": f"Invalid function name: {function_name!r}",
                        }
                    )
                    continue
                # Get the function to call
                function_to_call: Callable = name_to_function_map[function_name]
                # Try getting the function arguments
                try:
                    function_args_dict = json.loads(tool_call.function.arguments)
                except json.JSONDecodeError as exc:
                    # JSON decoding failed
                    print(f"Error decoding function arguments: {exc}")
                    messages.append(
                        {
                            "tool_call_id": tool_call.id,
                            "role": "tool",
                            "name": function_name,
                            "content": f"Error decoding function call `{function_name}` arguments {tool_call.function.arguments!r}! Error: {exc!s}",
                        }
                    )
                    continue
                # Call the selected function with generated arguments
                try:
                    print(
                        f"Calling function {function_name} with args: {json.dumps(function_args_dict)}"
                    )
                    function_response = function_to_call(**function_args_dict)
                    
                    print(
                        f"Function {function_name} returned: {function_response}"
                    )
                    # Extend conversation with function response
                    messages.append(
                        {
                            "tool_call_id": tool_call.id,
                            "role": "tool",
                            "name": function_name,
                            "content": function_response,
                        }
                    )
                except StopException as exc:
                    # Agent wants to stop the conversation (Expected)
                    print(f"Finish task with message: '{exc!s}'")
                    return messages
                except Exception as exc:
                    # Unexpected error calling function
                    print(
                        f"Error calling function `{function_name}`: {type(exc).__name__}: {exc!s}"
                    )
                    messages.append(
                        {
                            "tool_call_id": tool_call.id,
                            "role": "tool",
                            "name": function_name,
                            "content": f"Error calling function `{function_name}`: {type(exc).__name__}: {exc!s}!",
                        }
                    )
                    continue
    return messages


messages = run(messages)

print(len(messages))