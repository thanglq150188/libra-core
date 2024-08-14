from libra.models import ModelFactory
from libra.types import ModelLabel

if __name__ == "__main__":
    
    tools = [
        {
            "type": "function",
            "function": {
                "name": "add",
                "description": "Add two numbers together. Use this when you need to perform addition.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "num1": {
                            "type": "number",
                            "description": "The first number to add."
                        },
                        "num2": {
                            "type": "number",
                            "description": "The second number to add."
                        }
                    },
                    "required": ["num1", "num2"],
                    "additionalProperties": False
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "multiply",
                "description": "Multiply two numbers together. Use this when you need to perform multiplication.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "num1": {
                            "type": "number",
                            "description": "The first number to multiply."
                        },
                        "num2": {
                            "type": "number",
                            "description": "The second number to multiply."
                        }
                    },
                    "required": ["num1", "num2"],
                    "additionalProperties": False
                }
            }
        }
    ]
    
    from dotenv import load_dotenv
    
    load_dotenv(override=True)
    
    from libra.models.model_factory import ModelFactory
    from libra.config import ChatGPTConfig
    
    model = ModelFactory.create(
        model_label=ModelLabel.GPT_4o,
        model_config_dict=ChatGPTConfig(stream=True).__dict__,
    )
    
    # Prepare the input messages
    messages = [
        {"role": "user", "content": "ngọt ngào đến mấy cũng tan thành mây"}
    ]

    # Run the model with the input messages
    # response = model.stream(messages=messages, tools=tools)
    response = model.run(messages=messages)
    
    import json
    
    if model.stream:
        for chunk in response: # type: ignore
            content = chunk.choices[0].delta.content
            if content:
                print(content, end='')
    else:
        print(response.choices[0].message.content) # type: ignore
    
    print()