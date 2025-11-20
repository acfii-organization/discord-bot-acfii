from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:
    task_id: int
    title: str
    description: str
    assigned_to: str | None
    status: str
    created_at: str
