from abc import ABC, abstractmethod
from typing import Any


class BaseEmbedding(ABC):
    r"""Abstract base class for text embedding functionalities."""
    
    @abstractmethod
    def embed_list(self, objs: list[str], **kwargs: Any) -> list[list[float]]:
        """
        Abstract method for embedding a list of text strings into a list of numerical vectors.

        Parameters:
            texts (list[str]): A list of text strings to be embedded.
            **kwargs (Any): Extra kwargs passed to the embedding API.

        Returns:
            list[list[float]]: A list that represents the
                generated embedding as a list of floating-point numbers.
        """
        pass
    
    def embed(
        self,
        obj: str,
        **kwargs: Any,
    ) -> list[float]:
        r"""Generates an embedding for the given text.

        Args:
            text: The text for which to generate the embedding.
            **kwargs (Any): Extra kwargs passed to the embedding API.

        Returns:
            list[float]: A list of floating-point numbers representing the
                generated embedding.
        """
        return self.embed_list([obj], **kwargs)[0]
    
    @abstractmethod
    def get_output_dim(self) -> int:
        r"""Returns the output dimension of the embeddings.
        
        Returns:
            int: The dimensionality of the embeddings for the current model.
        """
        pass