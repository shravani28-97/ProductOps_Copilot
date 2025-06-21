# ProductOps Copilot

A LangGraph-powered multi-agent system that automates three routine product-management tasks:

1. **Feedback triage** – clusters user tickets, reviews, and survey verbatims into clear opportunity briefs.  
2. **Prioritization** – scores each opportunity with a cost-of-delay × effort model and returns a transparent stack-rank.  
3. **Experiment prep** – designs and runs simulated A/B tests with LLM personas to filter out low-impact ideas before live development.

---

## Table of Contents
- [Architecture](#architecture)
- [Feature Highlights](#feature-highlights)
- [Tech Stack](#tech-stack)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Local Development](#local-development)
- [Testing](#testing)
- [Deployment](#deployment)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [References](#references)

---

## Architecture
```
Ingestion Worker ─► Voice-of-Customer Synthesizer ─► Opportunity Scorer ─► Top-N Filter
        ▲                      │  ▲                                  │
        │                      │  └─ retry on low cohesion           │
        └───────────────┐      │                                     │
                        │      ▼                                     │
                Roadmap Negotiator ◄──────── SimTest Designer & Runner
                        │
                        ▼
                 PM Chat Interface
```

| Layer | Responsibility | Implementation |
|-------|----------------|----------------|
| **Ingestion Worker** | Pulls fresh data from Zendesk, Jira, Intercom, CSV drops | Airbyte tap → Pandas |
| **VoC Synthesizer** | Embeds, clusters, and labels feedback | OpenAI `text-embedding-3-large` + HDBSCAN + GPT labeling |
| **Opportunity Scorer** | Estimates impact and effort; returns RICE-style score | LightGBM (lift) + LangChain GitHub-effort tool |
| **SimTest Designer & Runner** | Generates synthetic personas and runs page flows | AgentA/B reference code |
| **Roadmap Negotiator** | Drafts one-page RFCs and decision logs | Retrieval-augmented GPT-4o |
| **PM Chat** | Natural-language interface over the whole state graph | FastAPI endpoint + LangGraph streaming |

---

## Feature Highlights
- **Stateful orchestration** with **LangGraph** – loops, branches, and retries are explicit.  
- **Plug-and-play data connectors** via Airbyte; swap in CSVs during prototyping.  
- **Vector and graph storage** for quick retrieval of past decisions and OKRs.  
- **Observability** through TruLens or LangSmith – replay any run without re-processing data.  
- **Container-first deployment**: Docker Compose for local work, Helm chart for Kubernetes.

---

## Tech Stack

| Category | Tool / Library |
|----------|----------------|
| Orchestration | LangGraph 0.3 |
| LLM / Embeddings | OpenAI GPT-4o & `text-embedding-3-large` |
| ML / Scoring | LightGBM, scikit-learn |
| Storage | Chroma (vector), Neo4j (dependency graph) |
| Data ingestion | Airbyte |
| Backend | FastAPI |
| Frontend (optional) | Next.js + shadcn/ui |
| Observability | TruLens, LangSmith |
| CI/CD | GitHub Actions, Docker, Helm |

---

## Quick Start

~~~bash
# 1. Clone
git clone https://github.com/<your-org>/productops-copilot.git
cd productops-copilot

# 2. Set up virtual environment
python -m venv .venv && source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Export your OpenAI key
export OPENAI_API_KEY=<key>

# 5. Run a local end-to-end pass
python scripts/run_once.py --tickets data/sample_zendesk.parquet
~~~

The script ingests the sample ticket dump, produces ten scored opportunities, and writes RFC drafts to `outputs/`.

---

## Configuration

All runtime settings live in `.env` (copy from `.env.example`):

~~~env
OPENAI_API_KEY=
VECTOR_STORE_PATH=.chroma/
AIRBYTE_CONFIG_PATH=airbyte/config/
TOP_N=10
~~~

Environment variables override CLI flags and default values in `config.py`.

---

## Local Development

~~~bash
# Start LangGraph ASGI app with hot reload
uvicorn copilot.graph:app --reload

# Open a second shell for the chat client
python scripts/ask.py "Why is Dark Mode below Single Sign-On?"
~~~

Logs and intermediate state snapshots appear under `.runs/`.

---

## Testing

~~~bash
pytest -q
pytest --cov=copilot --cov-report=term-missing
~~~

Unit tests stub external API calls and run on CPU-only machines. Add fixtures for new agent nodes in `tests/fixtures/`.

---

## Deployment

| Environment | Command |
|-------------|---------|
| **Docker Compose** | `docker compose up --build` |
| **Kubernetes** | `helm install copilot charts/` |
| **LangGraph Cloud** | `langgraph deploy` |

Set secrets (`OPENAI_API_KEY`, database URLs) through the platform’s secret manager or a Kubernetes `Secret`.

---

## Roadmap

- [ ] Streaming WebSocket endpoint for real-time chat updates  
- [ ] Fine-tune an embedding model on historical feedback to cut token spend  
- [ ] “Risk Radar” compliance agent  
- [ ] Competitive Intel watcher  
- [ ] Grafana dashboard with time-to-insight and backlog-churn KPIs  

---

## Contributing

1. Fork the repo and create a feature branch.  
2. Follow the **pre-commit** hooks (`black`, `ruff`, `isort`).  
3. Submit a pull request describing your change and link any related issue.  
4. A maintainer reviews and merges after CI passes.

---

## License

Distributed under the MIT License. See `LICENSE` for details.

---

## References
- LangGraph docs – <https://docs.langchain.com/langgraph>  
- AgentA/B: simulated user-persona A/B testing – <https://github.com/agentab/agentab>  
- Intercom Product Management blog – RICE scoring model
