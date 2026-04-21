from dataclasses import dataclass, field
from typing import Literal


@dataclass
class CommandResult:
    kind: Literal[
        "quit", "clear", "chat", "info", "error", "noop", "set_model", "set_active_file"
    ]
    content: str = ""
    data: dict = field(default_factory=dict)
