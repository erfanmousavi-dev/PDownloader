from textual import work
from textual.widgets import (
    Label,
    Input,
    ListView,
    ListItem,
    Button,
)

from src.ui.screens.base import BaseScreen
from src.services.downloader import Downloader


class AddLinksScreen(BaseScreen):

    BINDINGS = [
        *BaseScreen.BINDINGS,
        ("r", "remove_link", "Remove selected link"),
        ("escape", "go_home", "Back"),
    ]

    def __init__(self, link_manager, settings):

        super().__init__()

        self.link_manager = link_manager
        self.settings = settings
        self.downloader = None

    def screen_content(self):

        yield Label("Add Links Screen")

        yield Input(
            placeholder="Paste links separated by space or comma...",
            id="link_input",
        )

        yield ListView(id="links_list")

        yield Button(
            "Download",
            id="download",
        )

    def on_mount(self):

        self.downloader = Downloader(
            self.settings,
            self.app.progress_manager,
        )

        self.update_links_list()

    def on_input_submitted(self, event: Input.Submitted):

        links = self.parse_links(event.value)

        for link in links:
            self.link_manager.add(link)

        self.update_links_list()

        event.input.value = ""

        self.app.notify(
            f"{len(links)} link(s) added"
        )

    def parse_links(self, text):

        text = text.replace(",", " ")

        return text.split()

    def update_links_list(self):

        links_list = self.query_one("#links_list")

        links_list.clear()

        for index, link in enumerate(self.link_manager.get_all()):

            links_list.append(
                ListItem(
                    Label(f"{index + 1}. {link}")
                )
            )

    @work(thread=True)
    def start_download(self, links):

        self.downloader.download(links)

    def on_button_pressed(self, event: Button.Pressed):

        if event.button.id != "download":

            return

        links = self.link_manager.get_all()

        if not links:

            self.app.notify(
                "No links to download"
            )

            return

        self.start_download(
            links.copy()
        )

        self.app.notify(
            "Download started"
        )

    def action_remove_link(self):

        links_list = self.query_one("#links_list")

        if links_list.index is None:

            self.app.notify(
                "No link selected"
            )

            return

        index = links_list.index

        link = self.link_manager.get_all()[index]

        self.link_manager.remove(link)

        self.update_links_list()

        self.app.notify(
            "Link removed"
        )

    def action_go_home(self):

        self.app.pop_screen()