from libra.types.enums import ModelLabel, ModelCompany
from libra.models.base_model import ModelBackend
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
    
    
