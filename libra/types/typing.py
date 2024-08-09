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
    def company(self) -> ModelCompany:
        if self in {ModelLabel.GPT_4o, 
                    ModelLabel.GPT_4o_mini, 
                    ModelLabel.GPT_4_TURBO, 
                    ModelLabel.GPT_4, 
                    ModelLabel.GPT_4_TURBO,
                    ModelLabel.GPT_3_5_TURBO}:
            return ModelCompany.OPENAI
        elif self in {ModelLabel.AZURE_GPT_4o}:
            return ModelCompany.AZURE
        return ModelCompany.AZURE
    
    
class EmbeddingModelType(Enum):
    TEXT_EMBEDDING_ADA_2 = "text-embedding-ada-002"
    TEXT_EMBEDDING_3_SMALL = "text-embedding-3-small"
    TEXT_EMBEDDING_3_LARGE = "text-embedding-3-large"
    
    @property
    def is_openai(self) -> bool:
        r"""Returns whether this type of models is an OpenAI-released model."""
        return self in {
            EmbeddingModelType.TEXT_EMBEDDING_ADA_2,
            EmbeddingModelType.TEXT_EMBEDDING_3_SMALL,
            EmbeddingModelType.TEXT_EMBEDDING_3_LARGE,
        }
    
    @property
    def output_dim(self) -> int:
        if self is EmbeddingModelType.TEXT_EMBEDDING_ADA_2:
            return 1536
        elif self is EmbeddingModelType.TEXT_EMBEDDING_3_SMALL:
            return 1536
        elif self is EmbeddingModelType.TEXT_EMBEDDING_3_LARGE:
            return 3072
        else:
            raise ValueError(f"Unknown model type {self}.")


__all__ = ["ModelLabel", "ModelCompany", "EmbeddingModelType"]
