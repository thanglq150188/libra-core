import os
import requests
from libra.types import ModelLabel, ChatCompletion, ChatCompletionChunk
from libra.messages import OpenAIMessage
from openai import AzureOpenAI, Stream, AsyncAzureOpenAI
from typing import Dict, Any, List, Union
from libra.models.base_model import ModelBackend


class AzureOpenAIModel(ModelBackend):
    
    r"""Azure OpenAI API in a unified ModelBackend interface."""

    def __init__(self, model_label: ModelLabel, model_config_dict: Dict) -> None:
        """
        Initializes an instance of AzureOpenAIModel with the provided model label and configuration dictionary.

        Parameters:
        - model_label (ModelLabel): The label of the model to be used.
        - model_config_dict (Dict): A dictionary containing configuration parameters for the model.

        Returns:
        - None: This method does not return any value.

        Raises:
        - None: This method does not raise any exceptions.

        Note:
        - This method initializes the AzureOpenAI client using the provided API key from the environment variables.
        """
        super().__init__()
        self.model_label = model_label
        self.model_config_dict = model_config_dict
        self._client = AzureOpenAI(
            api_version=os.environ.get('AZURE_API_VERSION'),
            azure_endpoint=os.environ.get('AZURE_ENDPOINT') # type: ignore
        )
        self._async_client = AsyncAzureOpenAI(
            api_version=os.environ.get('AZURE_API_VERSION'),
            azure_endpoint=os.environ.get('AZURE_ENDPOINT') # type: ignore
        )

    
    def run(
        self,
        messages: List[OpenAIMessage], # type: ignore
    ) -> Union[ChatCompletion, Stream[ChatCompletionChunk]]: # type: ignore
        r"""Runs inference of Azure OpenAI chat completion.

        Args:
            messages (List[OpenAIMessage]): Message list with the chat history
                in OpenAI API format.

        Returns:
            Union[ChatCompletion, Stream[ChatCompletionChunk]]:
                `ChatCompletion` in the non-stream mode, or
                `Stream[ChatCompletionChunk]` in the stream mode.
        """
        response = self._client.chat.completions.create(
            messages=messages,
            model=self.model_label.value,
            **self.model_config_dict,
        )
        return response
    
    
    async def run_async(
        self,
        messages: List[OpenAIMessage], # type: ignore
    ) -> Union[ChatCompletion, Stream[ChatCompletionChunk]]: # type: ignore
        r"""Runs inference of Azure OpenAI chat completion asynchronously.

        Args:
            messages (List[OpenAIMessage]): Message list with the chat history
                in OpenAI API format.

        Returns:
            Union[ChatCompletion, Stream[ChatCompletionChunk]]:
                `ChatCompletion` in the non-stream mode, or
                `Stream[ChatCompletionChunk]` in the stream mode.
        """
        response = await self._async_client.chat.completions.create(
            messages=messages,
            model=self.model_label.value,
            **self.model_config_dict,
        )
        return response
    

    @property
    def stream(self) -> bool:
        r"""Returns whether the model is in stream mode,
            which sends partial results each time.
        Returns:
            bool: Whether the model is in stream mode.
        """
        return self.model_config_dict.get('stream', False)