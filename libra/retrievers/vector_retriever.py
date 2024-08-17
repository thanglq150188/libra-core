from typing import Any, Dict, List, Optional

from libra.embeddings import BaseEmbedding, OpenAIEmbedding
from libra.retrievers.base import BaseRetriever
from libra.vectordb import (
    BaseVectorStorage,
    QdrantStorage,
    VectorDBQuery,
    VectorRecord,
)

DEFAULT_TOP_K_RESULTS = 1
DEFAULT_SIMILARITY_THRESHOLD = 0.0


class VectorRetriever(BaseRetriever):
    r"""An implementation of the `BaseRetriever` by using vector storage and
    embedding model.

    This class facilitates the retriever of relevant information using a
    query-based approach, backed by vector embeddings.

    Attributes:
        embedding_model (BaseEmbedding): Embedding model used to generate
            vector embeddings.
        storage (BaseVectorStorage): Vector storage to query.
        similarity_threshold (float, optional): The similarity threshold
            for filtering results. Defaults to `DEFAULT_SIMILARITY_THRESHOLD`.
        unstructured_modules (UnstructuredIO): A module for parsing files and
            URLs and chunking content based on specified parameters.
    """

    def __init__(
        self,
        similarity_threshold: float = DEFAULT_SIMILARITY_THRESHOLD,
        embedding_model: Optional[BaseEmbedding] = None,
        storage: Optional[BaseVectorStorage] = None,
    ) -> None:
        r"""Initializes the retriever class with an optional embedding model.

        Args:
            similarity_threshold (float, optional): The similarity threshold
                for filtering results. Defaults to
                `DEFAULT_SIMILARITY_THRESHOLD`.
            embedding_model (Optional[BaseEmbedding]): The embedding model
                instance. Defaults to `OpenAIEmbedding` if not provided.
            storage (BaseVectorStorage): Vector storage to query.
        """
        self.embedding_model = embedding_model or OpenAIEmbedding()
        self.storage = (
            storage
            if storage is not None
            else QdrantStorage(
                vector_dim=self.embedding_model.get_output_dim()
            )
        )
        self.similarity_threshold = similarity_threshold

    def process(
        self,
        data: List[Dict[str, str]],
        batch_size: int = 10
    ) -> None:
        from tqdm import tqdm
        r"""Processes content from list of string, and stores their embeddings in the specified
        vector storage.

        Args:
            content_input_path (str): File path or URL of the content to be
                processed.
            chunk_type (str): Type of chunking going to apply. Defaults to
                "chunk_by_title".
            **kwargs (Any): Additional keyword arguments for content parsing.
        """
        # Iterate to process and store embeddings, set batch of 50
        for i in tqdm(range(0, len(data), batch_size)):
            batch_chunks = data[i : i + batch_size]
            batch_vectors = self.embedding_model.embed_list(
                objs=[chunk['embed'] for chunk in batch_chunks]
            )

            records = []
            # Prepare the payload for each vector record, includes the content
            # path, chunk metadata, and chunk text
            for vector, chunk in zip(batch_vectors, batch_chunks):
                payload = {
                    "metadata": {key: value for key, value in chunk.items() if key != 'content'},
                    "text": chunk['content']
                }
                # print(chunk_text)
                # print(vector)
                records.append(
                    VectorRecord(vector=vector, payload=payload)
                )

            self.storage.add(records=records)

    def query(
        self,
        query: str,
        top_k: int = DEFAULT_TOP_K_RESULTS,
    ) -> List[Dict[str, Any]]:
        r"""Executes a query in vector storage and compiles the retrieved
        results into a dictionary.

        Args:
            query (str): Query string for information retriever.
            top_k (int, optional): The number of top results to return during
                retriever. Must be a positive integer. Defaults to 1.

        Returns:
            List[Dict[str, Any]]: Concatenated list of the query results.

        Raises:
            ValueError: If 'top_k' is less than or equal to 0, if vector
                storage is empty, if payload of vector storage is None.
        """

        if top_k <= 0:
            raise ValueError("top_k must be a positive integer.")

        # Load the storage incase it's hosted remote
        self.storage.load()

        query_vector = self.embedding_model.embed(obj=query)
        db_query = VectorDBQuery(query_vector=query_vector, top_k=top_k)
        query_results = self.storage.query(query=db_query)

        if query_results[0].record.payload is None:
            raise ValueError(
                "Payload of vector storage is None, please check the "
                "collection."
            )

        # format the results
        formatted_results = []
        for result in query_results:
            if (
                result.similarity >= self.similarity_threshold
                and result.record.payload is not None
            ):
                result_dict = {
                    'similarity score': str(result.similarity),
                    'content path': result.record.payload.get(
                        'content path', ''
                    ),
                    'metadata': result.record.payload.get('metadata', {}),
                    'text': result.record.payload.get('text', ''),
                }
                formatted_results.append(result_dict)

        content_path = query_results[0].record.payload.get('content path', '')

        if not formatted_results:
            return [
                {
                    'text': (
                        f"No suitable information retrieved "
                        f"from {content_path} with similarity_threshold"
                        f" = {self.similarity_threshold}."
                    )
                }
            ]
        return formatted_results
