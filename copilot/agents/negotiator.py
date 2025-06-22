# copilot/agents/negotiator.py

from copilot.data_models import CopilotState

def roadmap_negotiator(state: CopilotState) -> CopilotState:
    """
    Stub: produce RFCs for each item in state.top_n
    """
    # e.g., append a one-line summary to chat_history
    for opp in state.top_n:
        state.chat_history.append({"role":"assistant", "content":f"RFC for {opp['title']}"})
    return state