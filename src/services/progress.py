from datetime import datetime
import threading

from src.models.download import Download


class ProgressManager:

    def __init__(self, app=None):

        self.app = app
        self.downloads = []
        self.logs = []
        self.log_callback = None


    def create(self, url):

        download = Download(url)

        self.downloads.append(download)

        self.log(
            f"Created download: {url}"
        )

        return download


    def hook(self, download):

        def callback(data):

            if self.app:

                self.app.call_from_thread(
                    self._update_download,
                    download,
                    data,
                )

            else:

                self._update_download(
                    download,
                    data,
                )

        return callback


    def _update_download(self, download, data):

        download.update(data)


    def log(self, message):

        timestamp = datetime.now().strftime(
            "%H:%M:%S"
        )

        entry = (
            f"[{timestamp}] {message}"
        )

        self.logs.append(entry)

        print(entry)

        if self.log_callback:

            if self.app:

                if threading.get_ident() == self.app._thread_id:

                    self.log_callback(entry)

                else:

                    self.app.call_from_thread(
                        self.log_callback,
                        entry,
                    )

            else:

                self.log_callback(entry)


    def notify(self, message):

        self.log(
            f"NOTIFY: {message}"
        )

        if self.app:

            self.app.notify(message)


    def get_logs(self):

        return self.logs


    def clear_logs(self):

        self.logs.clear()


    def set_log_callback(self, callback):

        self.log_callback = callback


    def get_all(self):

        return self.downloads