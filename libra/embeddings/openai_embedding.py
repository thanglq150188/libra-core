from __future__ import annotations

import os
from typing import Any

from openai import NOT_GIVEN, NotGiven, OpenAI, AsyncOpenAI

from libra.embeddings.base import BaseEmbedding
from libra.types import EmbeddingLabel
import asyncio


import sys

def set_event_loop_policy():
    if sys.platform.startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    elif sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
        asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
    else:
        print(f"Unsupported platform: {sys.platform}")
        sys.exit(1)

set_event_loop_policy()


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
        model_type: EmbeddingLabel = (
            EmbeddingLabel.TEXT_EMBEDDING_3_LARGE
        ),
        api_key: str | None = None,
        dimensions: int | NotGiven = NOT_GIVEN,
    ) -> None:
        if not model_type.of_company:
            raise ValueError("Invalid OpenAI embedding model type.")
        self.model_type = model_type
        if dimensions == NOT_GIVEN:
            self.output_dim = model_type.output_dim
        else:
            assert isinstance(dimensions, int)
            self.output_dim = dimensions
        self._api_key = api_key or os.environ.get("OPENAI_API_KEY")
        self.client = OpenAI(timeout=60, max_retries=3, api_key=self._api_key)
        self.async_client = AsyncOpenAI(timeout=60, max_retries=3, api_key=self._api_key)

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
    
    async def async_embed_list(
        self,
        objs: list[str],
        **kwargs: Any,
    ) -> list[list[float]]:
        r"""Asynchronously generates embeddings for the given texts.

        Args:
            objs (list[str]): The texts for which to generate the embeddings.
            **kwargs (Any): Extra kwargs passed to the embedding API.

        Returns:
            list[list[float]]: A list that represents the generated embedding
                as a list of floating-point numbers.
        """
        # TODO: count tokens
        response = await self.async_client.embeddings.create(
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
    import asyncio
    from dotenv import load_dotenv
    
    load_dotenv()
    
    openai_embedding = OpenAIEmbedding()
    print(openai_embedding.embed_list(["Cuộc sống không có bất cứ điều gì vui hết ?"]))
    print(openai_embedding.get_output_dim())

    async def test_async_embed():
        result = await openai_embedding.async_embed_list(["Cuộc sống không có bất cứ điều gì vui hết ?"])
        print(result)

    asyncio.run(test_async_embed())