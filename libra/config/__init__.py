from .base_config import BaseConfig
from .common_config import CommonConfig

from .openai_config import (
    OPENAI_API_PARAMS,
    ChatGPTConfig,
    OpenSourceConfig,
)

CHATGPT_CONFIG = ChatGPTConfig(
    stream=True,
    temperature=0.0,
    top_p=0.00001
)
COMMON_CONFIG = CommonConfig()

__all__ = [
    'BaseConfig',
    'ChatGPTConfig',
    'OPENAI_API_PARAMS',
    'OpenSourceConfig',
]
