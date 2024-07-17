# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "CompletionCreateParams",
    "Message",
    "MessageSystemMessageRequest",
    "MessageUserMessageRequest",
    "MessageUserMessageRequestContentUnionMember1",
    "MessageAssistantMessageRequest",
]


class CompletionCreateParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]

    model: Required[Literal["llama3-8b-8192"]]

    max_tokens: Optional[int]
    """
    The maximum number of [tokens](/tokenizer) that can be generated in the
    completion. The token count of your plus `max_tokens` cannot exceed the model's
    context length.
    """

    seed: Optional[int]
    """
    If specified, our system will make a best effort to sample deterministically,
    such that repeated requests with the same `seed` and parameters should return
    the same result. Determinism is not guaranteed.
    """

    stop: Union[str, List[str], None]
    """Up to 4 sequences where the API will stop generating further tokens.

    The returned text will not contain the stop sequence.
    """

    stream: Optional[bool]

    temperature: Optional[float]
    """What sampling temperature to use, between 0 and 2.

    Higher values like 0.8 will make the output more random, while lower values like
    0.2 will make it more focused and deterministic. We generally recommend altering
    this or `top_p` but not both.
    """

    top_p: Optional[float]
    """
    An alternative to sampling with temperature, called nucleus sampling, where the
    model considers the results of the tokens with top_p probability mass. So 0.1
    means only the tokens comprising the top 10% probability mass are considered. We
    generally recommend altering this or `temperature` but not both.
    """

    user: Optional[str]
    """
    A unique identifier representing your end-user, which can help Cerebras to
    monitor and detect abuse.
    """


class MessageSystemMessageRequest(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["system"]]

    name: Optional[str]


class MessageUserMessageRequestContentUnionMember1(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


class MessageUserMessageRequest(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageUserMessageRequestContentUnionMember1]]]

    role: Required[Literal["user"]]

    name: Optional[str]


class MessageAssistantMessageRequest(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["assistant"]]

    name: Optional[str]


Message = Union[MessageSystemMessageRequest, MessageUserMessageRequest, MessageAssistantMessageRequest]
