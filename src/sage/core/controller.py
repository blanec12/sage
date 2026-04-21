from sage.commands.interpreter import CommandInterpreter
from sage.core.actions import (
    AddAssistantMessageAction,
    AddUserMessageAction,
    ClearAction,
    ExitAction,
    UIAction,
)


class UIController:
    def __init__(self) -> None:
        self.interpreter = CommandInterpreter()

    def handle_input(self, text: str) -> list[UIAction]:
        stripped = text.strip()

        if not stripped:
            raise Exception("something fucked up")

        result = self.interpreter.handle(stripped)

        if result.kind == "quit":
            return [ExitAction()]

        if result.kind == "clear":
            return [ClearAction()]

        if result.kind == "info":
            return [AddAssistantMessageAction(result.content)]

        if result.kind == "error":
            return [AddAssistantMessageAction(f"Error: {result.content}")]

        if result.kind == "chat":
            return [AddUserMessageAction(stripped), AddAssistantMessageAction(stripped)]

        return [AddAssistantMessageAction("Error: could not handle input!")]
