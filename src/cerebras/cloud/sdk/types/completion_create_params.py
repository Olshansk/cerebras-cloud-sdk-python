# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["CompletionCreateParams", "StreamOptions"]


class CompletionCreateParams(TypedDict, total=False):
    model: Required[str]

    best_of: Optional[int]
    """
    Generates `best_of` completions server-side and returns the "best" (the one with
    the highest log probability per token). Results cannot be streamed. When used
    with `n`, `best_of` controls the number of candidate completions and `n`
    specifies how many to return – `best_of` must be greater than `n`. **Note:**
    Because this parameter generates many completions, it can quickly consume your
    token quota. Use carefully and ensure that you have reasonable settings for
    `max_tokens` and `stop`
    """

    echo: Optional[bool]
    """Echo back the prompt in addition to the completion"""

    frequency_penalty: Optional[float]
    """Number between -2.0 and 2.0.

    Positive values penalize new tokens based on their existing frequency in the
    text so far, decreasing the model's likelihood to repeat the same line verbatim.
    """

    logit_bias: Optional[object]
    """Modify the likelihood of specified tokens appearing in the completion.

    Accepts a JSON object that maps tokens (specified by their token ID in the
    tokenizer) to an associated bias value from -100 to 100. Mathematically, the
    bias is added to the logits generated by the model prior to sampling. The exact
    effect will vary per model, but values between -1 and 1 should decrease or
    increase likelihood of selection; values like -100 or 100 should result in a ban
    or exclusive selection of the relevant token.
    """

    logprobs: Optional[bool]
    """Whether to return log probabilities of the output tokens or not.

    If true, returns the log probabilities of each output token returned in the
    content of message.
    """

    max_tokens: Optional[int]
    """The maximum number of tokens that can be generated in the chat completion.

    The total length of input tokens and generated tokens is limited by the model's
    context length.
    """

    n: Optional[int]
    """How many chat completion choices to generate for each input message.

    Note that you will be charged based on the number of generated tokens across all
    of the choices. Keep n as 1 to minimize costs.
    """

    presence_penalty: Optional[float]
    """Number between -2.0 and 2.0.

    Positive values penalize new tokens based on whether they appear in the text so
    far, increasing the model's likelihood to talk about new topics.
    """

    prompt: Union[str, List[str], Iterable[int], Iterable[Iterable[int]]]
    """
    The prompt(s) to generate completions for, encoded as a string, array of
    strings, array of tokens, or array of token arrays.
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

    stream_options: Optional[StreamOptions]

    suffix: Optional[str]
    """The suffix that comes after a completion of inserted text.

    (OpenAI feature, not supported)
    """

    temperature: Optional[float]
    """What sampling temperature to use, between 0 and 1.5.

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

    x_amz_cf_id: Annotated[str, PropertyInfo(alias="X-Amz-Cf-Id")]

    x_delay_time: Annotated[float, PropertyInfo(alias="X-delay-time")]


class StreamOptionsTyped(TypedDict, total=False):
    include_usage: Optional[bool]


StreamOptions: TypeAlias = Union[StreamOptionsTyped, Dict[str, object]]
