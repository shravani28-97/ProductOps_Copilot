# copilot/agents/voc_synth.py

from copilot.data_models import CopilotState

def voc_synthesizer(state: CopilotState) -> CopilotState:
    """
    Stub: cluster tickets into themes and write them
    into state.opportunities.
    """
    state.opportunities = [
        {"title": "Stub Opportunity 1", "examples": [], "sentiment": 0.0},
        {"title": "Stub Opportunity 2", "examples": [], "sentiment": 0.0},
    ]
    return state