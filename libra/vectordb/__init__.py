from .base import (
    BaseVectorStorage,
    VectorDBQuery,
    VectorDBQueryResult,
    VectorDBStatus,
    VectorRecord
)

import os

from dotenv import load_dotenv

load_dotenv(override=True)

from .qdrant import QdrantStorage

from .milvus import MilvusStorage

from qdrant_client import QdrantClient

qdrant_instance = QdrantClient(
    path=os.environ['LOCAL_QDRANT_PATH']
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
