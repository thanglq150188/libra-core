from libra.models import OpenAIModel
from libra.types import ModelLabel

if __name__ == "__main__":
    from dotenv import load_dotenv
    
    load_dotenv(override=True)
    
    model = OpenAIModel(ModelLabel.GPT_4o, {"temperature":0.0})
    
    # Prepare the input messages
    messages = [
        {"role": "user", "content": "chào em, anh đứng đây từ chiều"}
    ]

    # Run the model with the input messages
    response = model.stream(messages=messages)
    
    import json
    
    for chunk in response:
        print(json.loads(chunk)['choices'][0]['delta']['content'], end='')
    # print(response)