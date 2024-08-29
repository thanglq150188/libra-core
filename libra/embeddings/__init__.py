from .base import BaseEmbedding
from .openai_embedding import OpenAIEmbedding
from .sentence_transformers_embedding import SentenceTransformerEncoder

from libra.embeddings import SentenceTransformerEncoder

print('loading embedding model...', end='')
bge_instance = SentenceTransformerEncoder(model_name="BAAI/bge-m3")
print('finish!')

__all__ = [
    'BaseEmbedding',
    'OpenAIEmbedding',
    'SentenceTransformerEncoder',
    'bge_instance'
]