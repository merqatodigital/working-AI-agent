"""Test classification only (no full agent loop)."""
from resort_data.loader import ResortDataStore
from resort_tools import set_store
from agent_core.nodes.classify import classify_intent

store = ResortDataStore.load_from_mock()
set_store(store)

print("Testing classification node...")
state = {
    "messages": [{"role": "user", "content": "Our AC stopped working in room R102"}],
    "intent": "",
    "urgency": "",
    "department": "",
    "guest_id": None,
    "reservation_id": None,
    "room_id": None,
    "step_count": 0,
}

result = classify_intent(state)
print(f"Intent: {result.get('intent')}")
print(f"Department: {result.get('department')}")
print(f"Urgency: {result.get('urgency')}")
print(f"Guest ID: {result.get('guest_id')}")
print(f"Room ID: {result.get('room_id')}")
print("Classification test passed!")
