from src.models.download import Download


class ProgressManager:

    def __init__(self, app=None):

        self.app = app
        self.downloads = []


    def create(self, url):

        download = Download(url)
        self.downloads.append(download)
        return download


    def hook(self, download):

        def callback(data):

            if self.app:

                self.app.call_from_thread(
                    download.update,
                    data
                )

            else:

                download.update(data)

        return callback


    def notify(self, message):

        if self.app:

            self.app.call_from_thread(
                self.app.notify,
                message
            )


    def get_all(self):

        return self.downloads