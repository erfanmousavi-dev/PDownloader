from textual.screen import Screen
from textual.widgets import Header, Footer


class BaseScreen(Screen):

    BINDINGS = [
        ("1", "push_screen('home')", "Home"),
        ("2", "push_screen('add_links')", "Add Links"),
        ("3", "push_screen('options')", "Options"),
        ("d", "toggle_dark_mode", "Toggle dark mode"),
    ]


    def compose(self):

        yield Header(show_clock=True)
        yield from self.screen_content()
        yield Footer()

    def screen_content(self):
        pass

    def action_toggle_dark_mode(self):

        self.app.action_toggle_dark_mode()
