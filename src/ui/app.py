from textual.app import App

from src.ui.screens.home import HomeScreen
from src.ui.screens.add_links import AddLinksScreen
from src.ui.screens.options import OptionsScreen
from src.ui.screens.logs import LogsScreen

from src.models.links import LinkManager
from src.models.settings import Settings

from src.services.progress import ProgressManager


class PDownloader(App):

    BINDINGS = [
        ("1", "push_screen('home')", "Home"),
        ("2", "push_screen('add_links')", "Add Links"),
        ("3", "push_screen('options')", "Options"),
        ("4", "push_screen('logs')", "Logs"),
        ("d", "toggle_dark_mode", "Toggle dark mode"),
    ]

    SCREENS = {
        "home": HomeScreen,
    }


    def __init__(self):

        super().__init__()

        self.link_manager = LinkManager()

        self.settings = Settings()

        self.progress_manager = ProgressManager(self)


    def on_mount(self):

        self.install_screen(
            AddLinksScreen(
                self.link_manager,
                self.settings,
            ),
            "add_links",
        )

        self.install_screen(
            OptionsScreen(
                self.settings,
            ),
            "options",
        )

        self.install_screen(
            LogsScreen(),
            "logs",
        )

        self.push_screen("home")


    def action_toggle_dark_mode(self):

        self.theme = (
            "textual-dark"
            if self.theme == "textual-light"
            else "textual-light"
        )


    def update_download_progress(self, value, text):

        self.progress_manager.update(
            value,
            text,
        )