from dataclasses import dataclass
from typing import Union


@dataclass(frozen=True)
class ExitAction:
    pass


@dataclass(frozen=True)
class ClearAction:
    pass


@dataclass(frozen=True)
class AddUserMessageAction:
    text: str


@dataclass(frozen=True)
class AddAssistantMessageAction:
    text: str


UIAction = Union[
    ExitAction, ClearAction, AddUserMessageAction, AddAssistantMessageAction
]
