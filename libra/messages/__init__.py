from libra.types import (
    ChatCompletionAssistantMessageParam,
    ChatCompletionFunctionMessageParam,
    ChatCompletionMessageParam,
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
)

OpenAISystemMessage = ChatCompletionSystemMessageParam
OpenAIAssistantMessage = ChatCompletionAssistantMessageParam
OpenAIUserMessage = ChatCompletionUserMessageParam
OpenAIFunctionMessage = ChatCompletionFunctionMessageParam
OpenAIMessage = ChatCompletionMessageParam


__all__ = [
    'OpenAISystemMessage',
    'OpenAIAssistantMessage',
    'OpenAIUserMessage',
    'OpenAIFunctionMessage',
    'OpenAIMessage',
]
