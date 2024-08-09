from libra.types.typing import ModelLabel, ModelCompany
from libra.models.base import ModelBackend
from libra.models.openai_model import OpenAIModel
from libra.models.azure_model import AzureOpenAIModel
from typing import Dict

class ModelFactory:
    r"""Factory class for model backends.
    
    Raises:
        ValueError: in case the provided model type is unknown.
    """
    
    @staticmethod
    def create(
        model_label: ModelLabel,
        model_config_dict: Dict,        
    ) -> ModelBackend:
        model_company = model_label.company
        if model_company == ModelCompany.OPENAI:
            model_class = OpenAIModel
        elif model_company == ModelCompany.AZURE:
            model_class = AzureOpenAIModel
        return model_class(model_label, model_config_dict)
    
    
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
    
    model = ModelFactory.create(
        model_label=ModelLabel.AZURE_GPT_4o,
        model_config_dict={
            "temperature": 0.0
        },
    )
    
    # Prepare the input messages
    messages = [
        {"role": "user", "content": "haha, ta là chồn hôi, chồn hôi nhớ chưa!!!!"}
    ]

    # Run the model with the input messages
    # response = model.stream(messages=messages, tools=tools)
    response = model.stream(messages=messages)
    
    import json
    
    # print(response)
    # for func in json.loads(response)['choices'][0]['message']['tool_calls']:
    #     print(func)
    for chunk in response: # type: ignore
        chunk_delta = json.loads(chunk)['choices'][0]['delta']
        print(chunk_delta['content'], end='')
        # print(chunk)
    print()