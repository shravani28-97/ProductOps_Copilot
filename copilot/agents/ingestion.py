# copilot/agents/ingestion.py

from copilot.data_models import CopilotState

def ingest_feedback(state: CopilotState) -> CopilotState:
    """
    Stub: load raw feedback into state.raw_tickets.
    """
    # TODO: plug in Airbyte / pandas / API fetch here
    state.raw_tickets = []
    return state