# copilot/agents/top_n.py

from copilot.data_models import CopilotState
from copilot.config import TOP_N

def top_n_filter(state: CopilotState) -> CopilotState:
    """
    Keep only the top TOP_N items from state.scored,
    based on each dict’s 'score' field.
    """
    # sort descending by score, then take the first TOP_N
    sorted_ops = sorted(state.scored, key=lambda o: o.get("score", 0), reverse=True)
    state.top_n = sorted_ops[:TOP_N]
    return state