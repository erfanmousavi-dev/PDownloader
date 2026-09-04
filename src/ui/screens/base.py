from textual.screen import Screen
from textual.widgets import Header, Footer


class BaseScreen(Screen):

    BINDINGS = [
        ("1", "push_screen('home')", "Home"),
        ("2", "push_screen('add_links')", "Add Links"),
        ("3", "push_screen('options')", "Options"),
        ("4", "push_screen('logs')", "Logs"),
    ]


    def compose(self):

        yield Header()
        yield from self.screen_content()
        yield Footer()


    def screen_content(self):

        pass