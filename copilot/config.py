# copilot/config.py

import os
from dotenv import load_dotenv

# Load from .env (make sure .env is in .gitignore)
load_dotenv()

# === LLM keys ===
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "").strip()
ANTHROPIC_MODEL   = os.getenv("ANTHROPIC_MODEL", "claude-2.1").strip()

# === Core settings ===
TOP_N             = int(os.getenv("TOP_N", 10))

# === Paths for sidecar services ===
VECTOR_STORE_PATH = os.getenv("VECTOR_STORE_PATH", ".chroma/")
AIRBYTE_CONFIG_PATH = os.getenv("AIRBYTE_CONFIG_PATH", "airbyte/config/")