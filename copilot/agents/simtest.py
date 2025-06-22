# copilot/agents/simtest.py

from copilot.data_models import CopilotState

def simtest_runner(state: CopilotState) -> CopilotState:
    """
    Stub: run simulated A/B tests on state.top_n
    """
    state.sim_report = {}   # replace with real sim results
    return state