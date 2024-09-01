from abc import ABC, abstractmethod
from typing import List, Union
from openai import Stream
from libra.messages import OpenAIMessage
from libra.types import ChatCompletion, ChatCompletionChunk


class ModelBackend(ABC):
    r"""Base class for different model backends. 
    May be OpenAI API, a local LLM, a stub for unit tests, etc."""
    
    @abstractmethod
    def run(
        self,
        messages: List[OpenAIMessage], # type: ignore
    ) -> Union[ChatCompletion, Stream[ChatCompletionChunk]]: # type: ignore
        r"""Runs the query to the backend model.

        Args:
            messages (List[OpenAIMessage]): Message list with the chat history
                in OpenAI API format.

        Returns:
            Union[ChatCompletion, Stream[ChatCompletionChunk]]:
                `ChatCompletion` in the non-stream mode, or
                `Stream[ChatCompletionChunk]` in the stream mode.
        """
        pass
    
    @abstractmethod
    async def run_async(
        self,
        messages: List[OpenAIMessage], # type: ignore
    ) -> Union[ChatCompletion, Stream[ChatCompletionChunk]]: # type: ignore
        r"""Runs the query to the backend model asynchronously.

        Args:
            messages (List[OpenAIMessage]): Message list with the chat history
                in OpenAI API format.

        Returns:
            Union[ChatCompletion, Stream[ChatCompletionChunk]]:
                `ChatCompletion` in the non-stream mode, or
                `Stream[ChatCompletionChunk]` in the stream mode.
        """
        pass
    
    @property
    def stream(self) -> bool:
        r"""Returns whether the model is in stream mode,
            which sends partial results each time.

        Returns:
            bool: Whether the model is in stream mode.
        """
        return False