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
        {"role": "user", "content": "Lương Sơn Bá và Juliet có hợp nhau không?"}
    ]

    # Run the model with the input messages
    response = model.stream(messages=messages)
    
    import json
    
    for chunk in response: # type: ignore
        print(json.loads(chunk)['choices'][0]['delta']['content'], end='')
    print()