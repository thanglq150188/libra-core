from libra.models import AzureOpenAIModel
from libra.types import ModelLabel
from libra.config import ChatGPTConfig

if __name__ == "__main__":
    from dotenv import load_dotenv
    
    load_dotenv(override=True)
    
    model = AzureOpenAIModel(ModelLabel.AZURE_GPT_4o, ChatGPTConfig().__dict__)
    
    # Prepare the input messages
    messages = [
        {"role": "user", "content": "chào em, anh đứng đây từ chiều ?"}
    ]

    # Run the model with the input messages
    response = model.run(messages=messages)
    
    import json
    
    if model.stream:
        for chunk in response:
            print(chunk.json())
    else:
        print(response.json()) # type: ignore