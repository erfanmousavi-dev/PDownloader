class Download:

    def __init__(self, url):
        self.url = url
        self.title = url
        self.progress = 0
        self.speed = ""
        self.eta = ""
        self.status = "waiting"

    def update(self, data):

        if "filename" in data:
            self.title = data["filename"]

        if data["status"] == "downloading":

            self.status = "downloading"

            total = (data.get("total_bytes") or data.get("total_bytes_estimate"))

            if total:

                self.progress = (data["downloaded_bytes"] / total) * 100

            self.speed = data.get("_speed_str", "")
            self.eta = data.get("_eta_str", "")

        elif data["status"] == "finished":

            self.progress = 100
            self.status = "finished"
