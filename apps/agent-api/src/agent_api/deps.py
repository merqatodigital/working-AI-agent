from __future__ import annotations

from resort_data.loader import ResortDataStore
from resort_tools import set_store
from agent_core.graph import build_graph

_store: ResortDataStore | None = None
_agent = None


def get_store() -> ResortDataStore:
    global _store
    if _store is None:
        _store = ResortDataStore.load_from_mock()
        set_store(_store)
    return _store


def get_agent():
    global _agent
    if _agent is None:
        store = get_store()
        _agent = build_graph(store=store)
    return _agent
