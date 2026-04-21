from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Input

from sage.ui.widgets.sidebar import Sidebar
from sage.ui.widgets.chat_pane import ChatPane
from sage.ui.widgets.composer import Composer


class MainScreen(Screen):
    CSS_PATH = "../styles/main.css"

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Sidebar()
            with Vertical():
                yield ChatPane()
                yield Composer()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        text = event.value.strip()
        if not text:
            return

        chat = self.query_one(ChatPane)
        chat.add_message(text, role="user")

        event.input.value = ""
