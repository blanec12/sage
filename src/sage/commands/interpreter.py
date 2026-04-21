from sage.commands.parser import CommandParser
from sage.commands.result import CommandResult
from sage.commands.types import ParsedCommand

from pathlib import Path


class CommandInterpreter:
    def __init__(self) -> None:
        self.parser = CommandParser()

    def handle(self, text: str) -> CommandResult:
        parsed = self.parser.parse(text)
        return self.execute(parsed)

    def execute(self, parsed: ParsedCommand) -> CommandResult:
        if parsed.kind == "empty":
            return CommandResult(kind="noop")

        if parsed.kind == "chat":
            return CommandResult(kind="chat", content=parsed.raw)

        if parsed.kind == "command":
            match parsed.name:
                case "q":
                    return CommandResult(kind="quit")
                case "clear":
                    return CommandResult(kind="clear")
                case "help":
                    return CommandResult(
                        kind="info", content="Commands: :q, :clear, :help"
                    )
                case "model":
                    if not parsed.args:
                        return CommandResult(
                            kind="error", content="Usage: :model <name>"
                        )

                    model_name = parsed.args[0]
                    return CommandResult(
                        kind="set_model",
                        content=f"Model set to {model_name}",
                        data={"model": model_name},
                    )
                case "open":
                    if not parsed.args:
                        return CommandResult(
                            kind="error", content="Usage: :open <path>"
                        )
                    raw_path = " ".join(parsed.args)
                    path = Path(raw_path)

                    return CommandResult(
                        kind="set_active_file",
                        content=f"Active file set to {path}",
                        data={"path": path},
                    )
                case _:
                    return CommandResult(
                        kind="error", content=f"Unknown command: {parsed.name}"
                    )

        return CommandResult(kind="error", content="Could not handle input!")
