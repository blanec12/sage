from textual.widgets import Static
from pathlib import Path


class Sidebar(Static):
    def __init__(self) -> None:
        super().__init__(id="sidebar")

        self.working_dir: Path | None = None
        self.model: str = ""
        self.tokens_used: int = 0
        self.tokens_available: int = 0
        self.active_files: list[Path] = []
        self.context_files: list[Path] = []

    def set_state(
        self,
        working_dir: Path,
        model: str,
        tokens_used: int,
        tokens_available: int,
        active_files: list[Path],
        context_files: list[Path],
    ) -> None:
        self.working_dir = working_dir
        self.model = model
        self.tokens_used = tokens_used
        self.tokens_available = tokens_available
        self.active_files = active_files
        self.context_files = context_files
        self.render_sidebar()

    def set_working_dir(self, working_dir: Path) -> None:
        self.working_dir = working_dir
        self.render_sidebar()

    def set_model(self, model: str) -> None:
        self.model = model
        self.render_sidebar()

    def set_tokens_used(self, tokens_used: int) -> None:
        self.tokens_used = tokens_used
        self.render_sidebar()

    def set_tokens_available(self, tokens_available: int) -> None:
        self.tokens_available = tokens_available
        self.render_sidebar()

    def set_active_files(self, active_files: list[Path]) -> None:
        self.active_files = active_files
        self.render_sidebar()

    def set_context_files(self, context_files: list[Path]) -> None:
        self.context_files = context_files
        self.render_sidebar()

    def render_sidebar(self) -> None:
        active_files = self.active_files or ["none"]
        context_files = self.context_files or ["none"]
        self.update(
            "\n".join(
                [
                    f"[b]Working dir:[/b] {self.working_dir}",
                    f"[b]Model:[/b] {self.model}",
                    f"[b]Token Usage:[/b] {self.tokens_used}/{self.tokens_available}",
                    f"[b]Active files:[/b]",
                    *[f"- {file}" for file in active_files],
                    f"[b]Context files:[/b]",
                    *[f"- {file}" for file in context_files],
                    f"[b]Commands:[/b]",
                    ":q       Quit",
                    ":clear   Clear chat",
                ]
            )
        )
