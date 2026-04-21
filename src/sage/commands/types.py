from dataclasses import dataclass
from typing import Literal


@dataclass
class ParsedCommand:
    kind: Literal["command", "chat", "empty"]
    name: str = ""
    args: list[str] | None = None
    raw: str = ""
