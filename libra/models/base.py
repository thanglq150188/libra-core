from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, List


class ModelBackend(ABC):
    r"""Base class for different model backends. 
    May be OpenAI API, a local LLM, a stub for unit tests, etc."""
    
    @abstractmethod
    def run(self, *args, **kwargs) -> Dict[str,Any]:
        r"""Runs the query to the backend model.
        
        Raises:
            RuntimeError: If the return value from API
            is not a dict that is expected.
        
        Returns:
            Dict[str, Any]: All backends must return a dict in OpenAI format.
        """
        pass
    
    @abstractmethod
    def stream(self, *args, **kwargs):
        """
        A method to stream responses from the model backend.

        This method is intended to be overridden by subclasses to provide streaming capabilities.
        It should yield dictionaries representing the model's responses in real-time.

        Parameters:
        - *args: Variable length argument list. This is not used in this method, but it is included to allow for flexibility in method signature.
        - **kwargs: Arbitrary keyword arguments. This is not used in this method, but it is included to allow for flexibility in method signature.

        Returns:
        - Generator[Dict, Any, None]: A generator that yields dictionaries representing the model's responses.
            Each dictionary should be in the format expected by the OpenAI API.
            If the model does not support streaming, this method should yield None.

        Raises:
        - NotImplementedError: If this method is not overridden by a subclass.
        """
        pass