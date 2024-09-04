from __future__ import annotations

from dataclasses import asdict, dataclass, field

from libra.types import (
    ModelCompany,
    ModelLabel, 
    EmbeddingCompany,
    EmbeddingLabel,
    VectorDBLabel
)
from libra.config import BaseConfig


@dataclass(frozen=True)
class CommonConfig(BaseConfig):
    model: ModelLabel = ModelLabel.GPT_4o
    embedding: EmbeddingCompany = EmbeddingCompany.OPENAI
    vectordb: VectorDBLabel = VectorDBLabel.QDRANT
    window_size: int = 4
    reload_data: bool = False
    