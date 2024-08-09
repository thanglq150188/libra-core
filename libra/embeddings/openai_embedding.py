from typing import Any
import os

from openai import NOT_GIVEN, NotGiven, OpenAI

from libra.embeddings.base import BaseEmbedding
from libra.types import EmbeddingModelType


class OpenAIEmbedding(BaseEmbedding):
    r"""Provides text embedding functionalities using OpenAI's models.

    Args:
        model_type (EmbeddingModelType, optional): The model type to be
            used for text embeddings.
            (default: :obj:`TEXT_EMBEDDING_3_SMALL`)
        api_key (str, optional): The API key for authenticating with the
            OpenAI service. (default: :obj:`None`)
        dimensions (int, optional): The text embedding output dimensions.
            (default: :obj:`NOT_GIVEN`)

    Raises:
        RuntimeError: If an unsupported model type is specified.
    """
    
    def __init__(
        self,
        model_type: EmbeddingModelType = (
            EmbeddingModelType.TEXT_EMBEDDING_3_SMALL
        ),
        api_key: str | None = None,
        dimensions: int | NotGiven = NOT_GIVEN,
    ) -> None:
        if not model_type.is_openai:
            raise ValueError("Invalid OpenAI embedding model type.")
        
        self.model_type = model_type
        if dimensions == NOT_GIVEN:
            self.output_dim = model_type.output_dim
        else:
            assert isinstance(dimensions, int)
            self.output_dim = dimensions
        self._api_key = api_key or os.environ.get("OPENAI_API_KEY")
        self.client = OpenAI(timeout=60, max_retries=3, api_key=self._api_key)
        
        
    def embed_list(
        self,
        objs: list[str],
        **kwargs: Any,
    ) -> list[list[float]]:
        r"""Generates embeddings for the given texts.

        Args:
            objs (list[str]): The texts for which to generate the embeddings.
            **kwargs (Any): Extra kwargs passed to the embedding API.

        Returns:
            list[list[float]]: A list that represents the generated embedding
                as a list of floating-point numbers.
        """
        # TODO: count tokens
        response = self.client.embeddings.create(
            input=objs,
            model=self.model_type.value,
            dimensions=self.output_dim,
            **kwargs,
        )
        return [data.embedding for data in response.data]
    
    
    def get_output_dim(self) -> int:
        r"""Returns the output dimension of the embeddings.

        Returns:
            int: The dimensionality of the embedding for the current model.
        """
        return self.output_dim
    

if __name__ == '__main__':
    openai_embedding = OpenAIEmbedding()
    print(openai_embedding.embed_list(["Cuộc sống không có bất cứ điều gì vui hết ?"]))
    print(openai_embedding.get_output_dim())