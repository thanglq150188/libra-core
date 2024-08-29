from .base import (
    BaseVectorStorage,
    VectorDBQuery,
    VectorDBQueryResult,
    VectorDBStatus,
    VectorRecord
)

from .qdrant import QdrantStorage

from .milvus import MilvusStorage

from qdrant_client import QdrantClient

qdrant_instance = QdrantClient(
    path='./libra_qdrant.db'
)

__all__ = [
    'BaseVectorStorage',
    'VectorDBQuery',
    'VectorDBQueryResult',
    'MilvusStorage',
    'VectorRecord',
    'VectorDBStatus',
    "qdrant_instance",
    'QdrantStorage'
]
