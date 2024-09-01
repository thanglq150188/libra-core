from enum import Enum


class ModelCompany(Enum):
    OPENAI = "openai"
    AZURE = "azure"


class ModelLabel(Enum):
    GPT_4o = "gpt-4o"   
    GPT_4o_mini = "gpt-4o-mini"
    GPT_4_TURBO = "gpt-4-turbo"
    GPT_4 = "gpt-4"
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    AZURE_GPT_4o = "gpt-4o-base"
    
    @property
    def of_company(self) -> ModelCompany:
        if self in {ModelLabel.GPT_4o, 
                    ModelLabel.GPT_4o_mini, 
                    ModelLabel.GPT_4_TURBO, 
                    ModelLabel.GPT_4, 
                    ModelLabel.GPT_4_TURBO,
                    ModelLabel.GPT_3_5_TURBO}:
            return ModelCompany.OPENAI
        elif self in {ModelLabel.AZURE_GPT_4o}:
            return ModelCompany.AZURE
        else:
            raise ValueError(f"Unknown model type {self}.")
    
    
class EmbeddingCompany(Enum):
    OPENAI = "openai"
    OSS = "open_source"
    
    
class EmbeddingLabel(Enum):
    TEXT_EMBEDDING_ADA_2 = "text-embedding-ada-002"
    TEXT_EMBEDDING_3_SMALL = "text-embedding-3-small"
    TEXT_EMBEDDING_3_LARGE = "text-embedding-3-large"
    BGE_M3 = "bge-m3"
    
    @property
    def of_company(self) -> EmbeddingCompany:
        r"""Returns whether this type of models is an OpenAI-released model."""
        if self in {
            EmbeddingLabel.TEXT_EMBEDDING_ADA_2,
            EmbeddingLabel.TEXT_EMBEDDING_3_SMALL,
            EmbeddingLabel.TEXT_EMBEDDING_3_LARGE,
        }:
            return EmbeddingCompany.OPENAI
        elif self in {EmbeddingLabel.BGE_M3}:
            return EmbeddingCompany.OSS
        else:
            raise ValueError(f"Unknown model type {self}.")
        
    @property
    def output_dim(self) -> int:
        if self is EmbeddingLabel.TEXT_EMBEDDING_ADA_2:
            return 1536
        elif self is EmbeddingLabel.TEXT_EMBEDDING_3_SMALL:
            return 1536
        elif self is EmbeddingLabel.TEXT_EMBEDDING_3_LARGE:
            return 3072
        elif self is EmbeddingLabel.BGE_M3:
            return 1024
        else:
            raise ValueError(f"Unknown model type {self}.")
        
        
class VectorDBLabel(Enum):
    MILVUS = "MILVUS"
    QDRANT = "QDRANT"
        
        
class VectorDistance(Enum):
    r"""Distance metrics used in a vector database."""

    DOT = "dot"
    r"""Dot product. https://en.wikipedia.org/wiki/Dot_product"""

    COSINE = "cosine"
    r"""Cosine similarity. https://en.wikipedia.org/wiki/Cosine_similarity"""

    EUCLIDEAN = "euclidean"
    r"""Euclidean distance. https://en.wikipedia.org/wiki/Euclidean_distance"""


__all__ = [
    "ModelLabel",
    "ModelCompany",
    "EmbeddingCompany",
    "EmbeddingLabel",
    "VectorDBLabel",
    "VectorDistance"
]
