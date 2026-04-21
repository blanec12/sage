from textual.widgets import Static


class Message(Static):
    def __init__(self, text: str, role: str) -> None:
        super().__init__(text, classes=f"message {role}")
        self.border_title = "You:" if role == "user" else "Assistant:"
