# copilot/graph.py

from langgraph.graph import StateGraph, START
from copilot.data_models import CopilotState

# import the six agent functions by their real names
from copilot.agents.ingestion     import ingest_feedback
from copilot.agents.voc_synth     import voc_synthesizer
from copilot.agents.scorer        import opportunity_scorer
from copilot.agents.top_n         import top_n_filter
from copilot.agents.simtest       import simtest_runner
from copilot.agents.negotiator    import roadmap_negotiator

# 1) Create a StateGraph with your Pydantic schema
g = StateGraph(CopilotState)

# 2) Register each agent as a node
for fn in (
    ingest_feedback,
    voc_synthesizer,
    opportunity_scorer,
    top_n_filter,
    simtest_runner,
    roadmap_negotiator,
):
    g.add_node(fn)

# 3) Wire up the flow in order
g.add_edge(START,                "ingest_feedback")
g.add_edge("ingest_feedback",    "voc_synthesizer")
g.add_edge("voc_synthesizer",    "opportunity_scorer")
g.add_edge("opportunity_scorer", "top_n_filter")
g.add_edge("top_n_filter",       "simtest_runner")
g.add_edge("simtest_runner",     "roadmap_negotiator")

# 4) Compile to an ASGI app
app = g.compile()

# (optional) CLI smoke-test
if __name__ == "__main__":
    state = CopilotState()
    out = app.invoke(state)
    print("Final state:", out)
