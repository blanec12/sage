from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Input

from sage.ui.widgets.sidebar import Sidebar
from sage.ui.widgets.chat_pane import ChatPane
from sage.ui.widgets.composer import Composer

from sage.commands.interpreter import CommandInterpreter

from pathlib import Path


class MainScreen(Screen):
    CSS_PATH = "../styles/main.css"

    def __init__(self) -> None:
        super().__init__()
        self.interpreter = CommandInterpreter()

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

        sidebar = self.query_one(Sidebar)
        chat = self.query_one(ChatPane)
        composer = self.query_one(Composer)

        result = self.interpreter.handle(text)

        if result.kind == "quit":
            self.app.exit()
            return

        if result.kind == "clear":
            chat.clear_messages()
            composer.clear()
            return

        if result.kind == "info":
            chat.add_assistant_message(result.content)
            composer.clear()
            return

        if result.kind == "error":
            chat.add_assistant_message(f"Error: {result.content}")
            composer.clear()
            return

        if result.kind == "chat":
            chat.add_user_message(text)
            chat.add_assistant_message(text)

        if result.kind == "set_model":
            sidebar.set_model(result.data["model"])
            chat.add_assistant_message(result.content)
            composer.clear()
            return

        if result.kind == "set_active_file":
            sidebar.set_active_files(result.data["path"])
            chat.add_assistant_message(result.content)
            composer.clear()
            return

        composer.clear()
