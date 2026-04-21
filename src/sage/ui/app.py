from textual.app import App

from sage.ui.screens.main_screen import MainScreen


class SageApp(App):
    def on_mount(self) -> None:
        self.push_screen(MainScreen())
