import os
import requests
from libra.types.typing import ModelCompany, ModelLabel
from openai import OpenAI
from typing import Dict, Any
from libra.models.base import ModelBackend


class OpenAIModel(ModelBackend):
    
    r"""OpenAI API in a unified ModelBackend interface."""

    def __init__(self, model_label: ModelLabel, model_config_dict: Dict) -> None:
        """
        Initialize an instance of OpenAIModel.

        Parameters:
        - model_label (ModelLabel): The label of the model to be used. It should be one of the enum values from ModelLabel.
        - model_config_dict (Dict): A dictionary containing the configuration parameters for the model.

        Note:
        - This method does not set any API keys. The API key should be set in the environment variable 'OPENAI_API_KEY' before calling this method.

        Returns:
        - None: This method does not return any value.
        """
        super().__init__()
        self.model_label = model_label
        self.model_config_dict = model_config_dict
        self.client = OpenAI(
            api_key=os.environ.get('OPENAI_API_KEY')
        )                     
    
    def run(self, **kwargs) -> Dict[str, Any]:
        """
        Executes the model with the given parameters and returns the response.

        Parameters:
        - kwargs (Dict): A dictionary containing the parameters for the model.
            It should contain a 'messages' key, which is a list of dictionaries,
            each representing a message in the conversation. Each message dictionary
            should have a 'content' key, which is the content of the message.

        Returns:
        - Dict[str, Any]: The response from the model. It should be a dictionary
            in the OpenAI format.

        Raises:
        - RuntimeError: If the return value from OpenAI API is not a dictionary.
        """
        kwargs['model'] = self.model_label.value
        kwargs['stream'] = False
        kwargs.update(self.model_config_dict)
        completion = self.client.chat.completions.create(**kwargs)
        return completion.json()    
    
    def stream(self, **kwargs):
        """
        A method to stream responses from the model backend.

        This method uses the OpenAI API to generate responses in real-time.
        It sends a request to the OpenAI API with the provided parameters and yields the responses as they are received.

        Parameters:
        - kwargs (Dict): A dictionary containing the parameters for the model.
            It should contain a 'messages' key, which is a list of dictionaries,
            each representing a message in the conversation. Each message dictionary
            should have a 'content' key, which is the content of the message.
            Additional parameters can be passed to the OpenAI API, such as 'temperature', 'max_tokens', etc.

        Yields:
        - Dict: A dictionary representing the model's response.
            Each dictionary should be in the format expected by the OpenAI API.
            If the model does not support streaming, this method will yield None.

        Raises:
        - RuntimeError: If the OpenAI API returns an error or an unexpected response.
        """
        kwargs['model'] = self.model_label.value
        kwargs['stream'] = True
        kwargs.update(self.model_config_dict)
        generator = self.client.chat.completions.create(**kwargs)
        for chunk in generator:
            if chunk.choices[0].delta.content:
                yield chunk.json() 