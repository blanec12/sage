from textual.containers import VerticalScroll

from sage.ui.widgets.message import Message


class ChatPane(VerticalScroll):

    def __init__(self) -> None:
        super().__init__(id="chat-pane")

    def add_message(self, text: str, role: str) -> None:
        self.mount(Message(text, role=role))
        self.scroll_end(animate=False)
