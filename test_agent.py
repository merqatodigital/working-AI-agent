"""Quick test of the KAPWA agent graph."""
from resort_data.loader import ResortDataStore
from resort_tools import set_store, ALL_TOOLS
from agent_core.graph import build_graph

store = ResortDataStore.load_from_mock()
set_store(store)

print("Building graph...")
agent = build_graph(store=store, tools=ALL_TOOLS)
print("Graph compiled successfully.")

print()
print("Testing agent with AC complaint...")
result = agent.invoke(
    {
        "messages": [{"role": "user", "content": "Our AC stopped working in room R102"}],
        "intent": "",
        "urgency": "",
        "department": "",
        "guest_id": None,
        "reservation_id": None,
        "room_id": None,
        "proposed_action": None,
        "approval_required": False,
        "approval_type": None,
        "audit_entries": [],
        "brief_update": None,
        "current_step": "",
        "step_count": 0,
        "max_steps": 10,
    },
    config={"configurable": {"thread_id": "test-1"}},
)
print(f"Intent: {result.get('intent')}")
print(f"Department: {result.get('department')}")
print(f"Urgency: {result.get('urgency')}")
print(f"Steps taken: {result.get('step_count')}")
msgs = result.get("messages", [])
print(f"Total messages: {len(msgs)}")
if msgs:
    last = msgs[-1]
    content = last.content if hasattr(last, "content") else str(last)
    print(f"Final response: {content[:500]}")
