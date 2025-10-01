"""Model profile definitions used for budgeting token counts.

Sources:
- OpenAI GPT-4.1 and GPT-4.1 Preview token limits (https://platform.openai.com/docs/models)
- Google Gemini 2.0/2.5 token limits (https://ai.google.dev/gemini-api/docs/models/gemini#model-parameters)
"""

from __future__ import annotations

from dataclasses import dataclass

__all__ = [
    "ModelProfile",
    "gpt_pro_chat_fast",
    "gpt_pro_chat_thinking",
    "gpt5_api",
    "chatgpt_paste_safe",
    "gemini_25_pro",
    "ALL_PROFILES",
]


@dataclass(slots=True, frozen=True)
class ModelProfile:
    """Token and overlap characteristics for a target LLM deployment."""

    name: str
    input_limit: int
    output_limit: int
    safe_input_budget: int
    overlap_tokens: int


gpt_pro_chat_fast = ModelProfile(
    name="gpt-pro-fast",
    input_limit=128_000,
    output_limit=16_384,
    safe_input_budget=100_000,  # already conservative for 128k UI
    overlap_tokens=200,
)
"""OpenAI GPT Pro Chat Fast profile."""


gpt_pro_chat_thinking = ModelProfile(
    name="gpt-pro-thinking",
    input_limit=196_000,
    output_limit=16_384,
    # Many ChatGPT "Pro/Thinking" chats behave like 128k once UI overhead is included.
    # Lower to avoid "message too long" errors when copy-pasting.
    safe_input_budget=120_000,
    overlap_tokens=200,
)
"""OpenAI GPT Pro Chat Thinking profile."""


gpt5_api = ModelProfile(
    name="gpt5-api",
    # API models now advertise 400k context.
    input_limit=400_000,
    output_limit=128_000,
    safe_input_budget=320_000,  # leave room for instructions + output
    overlap_tokens=200,
)
"""OpenAI GPT-5 API profile."""


chatgpt_paste_safe = ModelProfile(
    name="chatgpt-paste-safe",
    input_limit=128_000,
    output_limit=16_384,
    safe_input_budget=110_000,  # ~85% of 128k to cover UI overhead + reply
    overlap_tokens=200,
)
"""OpenAI ChatGPT paste-safe profile."""


gemini_25_pro = ModelProfile(
    name="gemini-2.5-pro",
    input_limit=1_048_576,
    output_limit=65_536,
    safe_input_budget=950_000,
    overlap_tokens=300,
)
"""Google Gemini 2.5 Pro profile."""


ALL_PROFILES: dict[str, ModelProfile] = {
    profile.name: profile
    for profile in (
        gpt_pro_chat_fast,
        gpt_pro_chat_thinking,
        gpt5_api,
        chatgpt_paste_safe,
        gemini_25_pro,
    )
}
"""Lookup table of profile name to definition."""
