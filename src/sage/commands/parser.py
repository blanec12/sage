from sage.commands.types import ParsedCommand


class CommandParser:
    def parse(self, text: str) -> ParsedCommand:
        text = text.strip()

        if not text:
            return ParsedCommand(kind="empty", raw=text)

        if not text.startswith(":"):
            return ParsedCommand(kind="chat", raw=text)

        body = text[1:].strip()
        if not body:
            return ParsedCommand(kind="command", name="", args=[], raw=text)

        parts = body.split()
        name = parts[0]
        args = parts[1:]

        return ParsedCommand(kind="command", name=name, args=args, raw=text)
