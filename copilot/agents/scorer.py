# copilot/agents/scorer.py

from copilot.data_models import CopilotState

def opportunity_scorer(state: CopilotState) -> CopilotState:
    """
    Stub: add a 'score' field (0-100) to each opportunity.
    Replace with LightGBM or a RICE-style calculator later.
    """
    scored = []
    for i, opp in enumerate(state.opportunities, start=1):
        scored.append({**opp, "score": i * 10})   # 10, 20, 30, …
    state.scored = scored
    return state