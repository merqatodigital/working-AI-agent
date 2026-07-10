"""KAPWA Resort Agent — Interactive CLI for testing."""
from __future__ import annotations

import sys
from pathlib import Path

from resort_data.loader import ResortDataStore
from resort_tools import set_store
from agent_core.graph import build_graph


def main():
    print("=" * 60)
    print("  KAPWA Resort Super Agent v0.1")
    print("  Palawan Island, Philippines")
    print("=" * 60)
    print()

    print("Loading resort data...")
    store = ResortDataStore.load_from_mock()
    set_store(store)
    print(f"  Guests: {len(store.guests)}")
    print(f"  Rooms: {len(store.rooms)}")
    print(f"  Staff: {len(store.staff)}")
    print(f"  Reservations: {len(store.reservations)}")
    print()

    print("Building agent graph...")
    agent = build_graph(store=store)
    print("  Agent ready.")
    print()

    config = {"configurable": {"thread_id": "cli-session"}}

    print("Type a message to the agent (or 'quit' to exit):")
    print("-" * 60)
    print()

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            break

        try:
            result = agent.invoke(
                {"messages": [{"role": "user", "content": user_input}]},
                config=config,
            )

            messages = result.get("messages", [])
            if messages:
                last = messages[-1]
                content = last.content if hasattr(last, "content") else str(last)
                print(f"\nKAPWA: {content}")
            else:
                print("\nKAPWA: (no response)")

            intent = result.get("intent", "N/A")
            dept = result.get("department", "N/A")
            urgency = result.get("urgency", "N/A")
            print(f"  [intent: {intent} | dept: {dept} | urgency: {urgency}]")
            print()

        except Exception as e:
            print(f"\nError: {e}")
            print()


if __name__ == "__main__":
    main()
