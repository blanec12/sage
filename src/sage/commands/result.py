from dataclasses import dataclass
from typing import Literal


@dataclass
class CommandResult:
    kind: Literal["quit", "clear", "chat", "info", "error", "noop"]
    content: str = ""
