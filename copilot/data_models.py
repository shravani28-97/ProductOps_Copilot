# copilot/data_models.py

from pydantic import BaseModel, Field
from typing import List, Dict, Any

class CopilotState(BaseModel):
    raw_tickets: List[Dict[str, Any]]     = Field(default_factory=list)
    opportunities: List[Dict[str, Any]]   = Field(default_factory=list)
    scored: List[Dict[str, Any]]          = Field(default_factory=list)
    top_n: List[Dict[str, Any]]           = Field(default_factory=list)
    sim_report: Dict[str, Any]            = Field(default_factory=dict)
    chat_history: List[Dict[str, str]]    = Field(default_factory=list)