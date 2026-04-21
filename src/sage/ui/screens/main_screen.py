from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Input

from sage.ui.widgets.sidebar import Sidebar
from sage.ui.widgets.chat_pane import ChatPane
from sage.ui.widgets.composer import Composer

from sage.core.actions import (
    AddAssistantMessageAction,
    AddUserMessageAction,
    ClearAction,
    ExitAction,
    UIAction,
)
from sage.core.controller import UIController

from pathlib import Path


class MainScreen(Screen):
    CSS_PATH = "../styles/main.css"

    def __init__(self) -> None:
        super().__init__()
        self.controller = UIController()

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Sidebar()
            with Vertical():
                yield ChatPane()
                yield Composer()

    def on_mount(self) -> None:
        sidebar = self.query_one(Sidebar)
        sidebar.set_state(
            working_dir=Path.cwd().resolve(),
            model="mock-model_o1",
            tokens_used=0,
            tokens_available=200000,
            active_files=[Path("src/sage/ui/screens/main_screen.py")],
            context_files=[Path("PROJECT.md"), Path("ARCHITECTURE.md")],
        )

    def on_input_submitted(self, event: Input.Submitted) -> None:
        text = event.value.strip()
        if not text:
            return

        actions = self.controller.handle_input(text)
        for action in actions:
            self._apply_action(action)

    def _apply_action(self, action: UIAction) -> None:
        sidebar = self.query_one(Sidebar)
        chat = self.query_one(ChatPane)
        composer = self.query_one(Composer)

        if isinstance(action, ExitAction):
            self.app.exit()
            return

        if isinstance(action, ClearAction):
            chat.clear_messages()
            composer.clear()
            return

        if isinstance(action, AddAssistantMessageAction):
            chat.add_assistant_message(action.text)
            composer.clear()
            return

        if isinstance(action, AddUserMessageAction):
            chat.add_user_message(action.text)
            composer.clear()

        # composer.clear()
