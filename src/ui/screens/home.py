from textual.widgets import Label

from src.ui.screens.base import BaseScreen
from src.ui.widgets.progress_bar import DownloadProgress


class HomeScreen(BaseScreen):

    def screen_content(self):

        yield Label("\n")
        yield Label("Welcome to PDownloader!")
        yield Label("You can download videos/audio from many websites.")

    def on_mount(self):

        self.known_downloads = set()
        self.set_interval(0.5,self.update_downloads)

    def update_downloads(self):

        downloads = (self.app.progress_manager.get_all())

        for download in downloads:

            if download not in self.known_downloads:

                self.known_downloads.add(download)

                self.mount(DownloadProgress(download))
