from __future__ import annotations

import os
from pathlib import Path

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["settings"])

SETTINGS_FILE = Path(__file__).parent.parent.parent.parent.parent / "data" / "settings.json"


class LLMSettings(BaseModel):
    provider: str = "ollama"
    model: str = "qwen2.5:3b"
    base_url: str = "http://localhost:11434"
    api_key: str = ""
    temperature: float = 0.3


class OpenRouterModel(BaseModel):
    id: str
    name: str
    cost: str
    category: str  # "free", "paid", "local"


OPENROUTER_CATALOG: list[OpenRouterModel] = [
    # Local Ollama
    OpenRouterModel(id="ollama/qwen2.5:3b", name="Qwen2.5 3B (Local)", cost="Free", category="local"),
    OpenRouterModel(id="ollama/hermes3", name="Hermes 3 (Local)", cost="Free", category="local"),
    OpenRouterModel(id="ollama/ornith:9b", name="Ornith 9B (Local)", cost="Free", category="local"),
    # Free tier
    OpenRouterModel(id="qwen/qwen3-235b-a22b-2507", name="Qwen3 235B", cost="$0.07/1M", category="free"),
    OpenRouterModel(id="deepseek/deepseek-chat", name="DeepSeek V3", cost="$0.14/1M", category="free"),
    OpenRouterModel(id="mistralai/ministral-3b-2512", name="Ministral 3B", cost="$0.10/1M", category="free"),
    # Paid
    OpenRouterModel(id="openai/gpt-4.1-nano", name="GPT-4.1 Nano", cost="$0.10/1M", category="paid"),
    OpenRouterModel(id="google/gemini-2.0-flash-001", name="Gemini 2.0 Flash", cost="$0.10/1M", category="paid"),
    OpenRouterModel(id="anthropic/claude-3-haiku", name="Claude 3 Haiku", cost="$0.25/1M", category="paid"),
    OpenRouterModel(id="deepseek/deepseek-r1-0528", name="DeepSeek R1", cost="$0.50/1M", category="paid"),
    OpenRouterModel(id="openai/gpt-5-mini", name="GPT-5 Mini", cost="$0.25/1M", category="paid"),
    OpenRouterModel(id="qwen/qwen3-coder", name="Qwen3 Coder", cost="$0.22/1M", category="paid"),
    OpenRouterModel(id="xiaomi/mimo-v2-flash", name="MiMo V2 Flash", cost="$0.09/1M", category="paid"),
]

_current_settings = LLMSettings()


def _load_settings() -> LLMSettings:
    global _current_settings
    if SETTINGS_FILE.exists():
        import json
        with open(SETTINGS_FILE) as f:
            data = json.load(f)
        _current_settings = LLMSettings(**data)
    return _current_settings


def _save_settings(settings: LLMSettings) -> None:
    global _current_settings
    _current_settings = settings
    SETTINGS_FILE.parent.mkdir(parents=True, exist_ok=True)
    import json
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings.model_dump(), f, indent=2)


@router.get("/settings/models")
def list_available_models():
    return {"models": [m.model_dump() for m in OPENROUTER_CATALOG]}


@router.get("/settings/llm")
def get_llm_settings():
    settings = _load_settings()
    return {"settings": settings.model_dump()}


@router.post("/settings/llm")
def update_llm_settings(settings: LLMSettings):
    _save_settings(settings)
    os.environ["KAPWA_LLM_PROVIDER"] = settings.provider
    os.environ["KAPWA_LLM_MODEL"] = settings.model
    os.environ["KAPWA_LLM_BASE_URL"] = settings.base_url
    if settings.api_key:
        os.environ["OPENROUTER_API_KEY"] = settings.api_key
    return {"status": "ok", "settings": settings.model_dump()}


@router.get("/settings/ollama/status")
def check_ollama_status():
    import urllib.request
    import json
    base_url = _current_settings.base_url or "http://localhost:11434"
    try:
        req = urllib.request.Request(f"{base_url}/api/tags", method="GET")
        with urllib.request.urlopen(req, timeout=3) as resp:
            data = json.loads(resp.read())
            models = [m["name"] for m in data.get("models", [])]
            return {"status": "connected", "url": base_url, "models": models}
    except Exception as e:
        return {"status": "disconnected", "url": base_url, "error": str(e)}
