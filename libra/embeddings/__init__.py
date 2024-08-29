from .base import BaseEmbedding
from .openai_embedding import OpenAIEmbedding
from .sentence_transformers_embedding import SentenceTransformerEncoder

from libra.embeddings import SentenceTransformerEncoder
import os
from dotenv import load_dotenv

load_dotenv(override=True)


print('loading embedding model...', end='')
bge_instance = SentenceTransformerEncoder(model_name=os.environ["LOCAL_EMBEDDING_PATH"])
print('finish!')

__all__ = [
    'BaseEmbedding',
    'OpenAIEmbedding',
    'SentenceTransformerEncoder',
    'bge_instance'
]