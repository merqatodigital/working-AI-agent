from __future__ import annotations

import os
from enum import Enum

from pydantic import BaseModel


class LLMProvider(str, Enum):
    OLLAMA = "ollama"
    OPENROUTER = "openrouter"


class LLMConfig(BaseModel):
    provider: LLMProvider
    model: str
    base_url: str | None = None
    api_key: str | None = None
    temperature: float = 0.3


OLLAMA_LOCAL = LLMConfig(
    provider=LLMProvider.OLLAMA,
    model="qwen2.5:3b",
    base_url="http://localhost:11434",
)

OPENROUTER_FREE = LLMConfig(
    provider=LLMProvider.OPENROUTER,
    model="qwen/qwen3-235b-a22b-2507",
    base_url="https://openrouter.ai/api/v1",
)

OPENROUTER_CHEAP = LLMConfig(
    provider=LLMProvider.OPENROUTER,
    model="deepseek/deepseek-chat",
    base_url="https://openrouter.ai/api/v1",
)

OPENROUTER_CATALOG = {
    "local": [
        {"id": "ollama/qwen2.5:3b", "name": "Qwen2.5 3B (Local)", "cost": "Free"},
        {"id": "ollama/hermes3", "name": "Hermes 3 (Local)", "cost": "Free"},
    ],
    "free": [
        {"id": "qwen/qwen3-235b-a22b-2507", "name": "Qwen3 235B", "cost": "$0.07/1M"},
        {"id": "deepseek/deepseek-chat", "name": "DeepSeek V3", "cost": "$0.14/1M"},
        {"id": "mistralai/ministral-3b-2512", "name": "Ministral 3B", "cost": "$0.10/1M"},
    ],
    "paid": [
        {"id": "openai/gpt-4.1-nano", "name": "GPT-4.1 Nano", "cost": "$0.10/1M"},
        {"id": "google/gemini-2.0-flash-001", "name": "Gemini 2.0 Flash", "cost": "$0.10/1M"},
        {"id": "anthropic/claude-3-haiku", "name": "Claude 3 Haiku", "cost": "$0.25/1M"},
        {"id": "deepseek/deepseek-r1-0528", "name": "DeepSeek R1", "cost": "$0.50/1M"},
        {"id": "openai/gpt-5-mini", "name": "GPT-5 Mini", "cost": "$0.25/1M"},
    ],
}


def get_llm(config: LLMConfig | None = None):
    if config is None:
        config = _load_config_from_env()
    if config.provider == LLMProvider.OLLAMA:
        from langchain_ollama import ChatOllama
        return ChatOllama(
            model=config.model,
            base_url=config.base_url or "http://localhost:11434",
            temperature=config.temperature,
        )
    elif config.provider == LLMProvider.OPENROUTER:
        from langchain_openai import ChatOpenAI
        api_key = config.api_key or os.environ.get("OPENROUTER_API_KEY", "")
        return ChatOpenAI(
            model=config.model,
            base_url=config.base_url or "https://openrouter.ai/api/v1",
            api_key=api_key,
            temperature=config.temperature,
        )
    else:
        raise ValueError(f"Unknown provider: {config.provider}")


def _load_config_from_env() -> LLMConfig:
    provider = os.environ.get("KAPWA_LLM_PROVIDER", "ollama")
    model = os.environ.get("KAPWA_LLM_MODEL", "qwen2.5:3b")
    base_url = os.environ.get("KAPWA_LLM_BASE_URL")
    api_key = os.environ.get("OPENROUTER_API_KEY")
    return LLMConfig(
        provider=LLMProvider(provider),
        model=model,
        base_url=base_url,
        api_key=api_key,
    )
