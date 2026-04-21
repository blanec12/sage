from textual.widgets import Static
from pathlib import Path


class Sidebar(Static):
    def __init__(self) -> None:
        super().__init__(id="sidebar")

        self.project: Path | None = None
        self.model: str = ""
        self.tokens_used: int = 0
        self.tokens_available: int = 0
        self.active_file: Path | None = None
        self.context_files: list[Path] = []

    def set_state(
        self,
        project: Path,
        model: str,
        tokens_used: int,
        tokens_available: int,
        active_file: Path,
        context_files: list[Path],
    ) -> None:
        self.project = project
        self.model = model
        self.tokens_used = tokens_used
        self.tokens_available = tokens_available
        self.active_file = active_file
        self.context_files = context_files
        self.render_sidebar()

    def render_sidebar(self) -> None:
        context_lines = self.context_files or ["none"]
        self.update(
            "\n".join(
                [
                    f"[b]Project:[/b] {self.project}",
                    f"[b]Model:[/b] {self.model}",
                    f"[b]Token Usage:[/b] {self.tokens_used}/{self.tokens_available}",
                    f"[b]Active file:[/b] {self.active_file}",
                    f"[b]Context files:[/b]",
                    *[f"- {file}" for file in context_lines],
                    f"[b]Commands:[/b]",
                    ":q       Quit",
                    ":clear   Clear chat",
                ]
            )
        )
