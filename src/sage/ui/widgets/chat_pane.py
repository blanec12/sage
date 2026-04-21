from textual.widgets import Static


class ChatPane(Static):

    def __init__(self) -> None:
        super().__init__("Chat pane", id="chat-pane")
