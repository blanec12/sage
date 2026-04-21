from textual.containers import VerticalScroll

from sage.ui.widgets.message import Message


class ChatPane(VerticalScroll):
    def __init__(self) -> None:
        super().__init__(id="chat-pane")

    def add_message(self, text: str, role: str) -> None:
        self.mount(Message(text, role=role))
        self.scroll_end(animate=False)

    def add_user_message(self, text: str) -> None:
        self.add_message(text, role="user")

    def add_assistant_message(self, text: str) -> None:
        self.add_message(text, role="assistant")

    def clear_messages(self) -> None:
        for child in list(self.children):
            child.remove()
