"""Helpers for estimating and counting token usage across providers."""

from __future__ import annotations

import math
from functools import lru_cache
from typing import Callable, Tuple

import tiktoken

TokenCounter = Callable[[str], int]


@lru_cache(maxsize=1)
def _o200k_encoding() -> tiktoken.Encoding:
    return tiktoken.get_encoding("o200k_base")


def count_gpt5_tokens(text: str) -> int:
    """Count tokens using OpenAI's ``o200k_base`` tokenizer."""

    return len(_o200k_encoding().encode(text))


def estimate_gemini_tokens(text: str) -> int:
    """Estimate Gemini token usage by assuming four characters per token."""

    if not text:
        return 0
    return math.ceil(len(text) / 4)


def count_gemini_tokens_via_api(text: str) -> int:
    """Call the Gemini ``models.countTokens`` endpoint.

    See https://ai.google.dev/api/rest/v1/models/countTokens for the API reference.
    This function is a stub that should be implemented where network access is allowed.
    """

    raise NotImplementedError("Gemini token counting via API not implemented.")


def cap_to_budget(text: str, budget: int, tokenizer: TokenCounter) -> Tuple[int, bool]:
    """Return the token count and whether it fits within ``budget``."""

    token_count = tokenizer(text)
    return token_count, token_count <= budget
