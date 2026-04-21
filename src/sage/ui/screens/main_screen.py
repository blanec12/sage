from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import Screen

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
