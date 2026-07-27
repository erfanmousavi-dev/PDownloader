from textual.widgets import Static
from textual.containers import Vertical

class DownloadProgress(Vertical):

    def __init__(self, download):

        super().__init__()

        self.download = download
        self.label = Static()


    def compose(self):

        yield self.label


    def on_mount(self):

        self.set_interval(0.5, self.refresh_progress)


    def refresh_progress(self):

        d = self.download

        self.label.update(
            f"""
            {d.title}

            Status: {d.status}
            Progress: {d.progress:.1f}%

            Speed: {d.speed}
            ETA: {d.eta}
            """
        )
