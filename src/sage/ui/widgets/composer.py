from textual.widgets import Input


class Composer(Input):

    def __init__(self) -> None:
        super().__init__(placeholder="Type here...", id="composer")

    def clear(self) -> None:
        self.value = ""
