import yt_dlp


class YTDLPLogger:

    def __init__(self, progress_manager):

        self.progress_manager = progress_manager


    def debug(self, message):

        if message.startswith("[debug]"):

            return

        self.progress_manager.log(
            message
        )


    def warning(self, message):

        self.progress_manager.log(
            f"WARNING: {message}"
        )


    def error(self, message):

        self.progress_manager.log(
            f"ERROR: {message}"
        )


class Downloader:

    def __init__(self, settings, progress_manager=None):

        self.settings = settings
        self.progress_manager = progress_manager


    def download(self, links):

        self.log(
            "Downloader started"
        )

        for link in links:

            self.log(
                f"Processing: {link}"
            )

            if self.is_youtube_url(link):

                self.log(
                    "Detected YouTube URL"
                )

                if not self.settings.browser_cookies_enabled:

                    self.log(
                        "YouTube download skipped: "
                        "Browser cookies are disabled"
                    )

                    continue


            options = self.get_options(link)

            self.log(
                "Creating download task"
            )

            if self.progress_manager:

                download = (
                    self.progress_manager
                    .create(link)
                )

                options["progress_hooks"] = [
                    self.progress_manager.hook(download)
                ]


            try:

                self.log(
                    "Creating YoutubeDL instance"
                )

                with yt_dlp.YoutubeDL(options) as ydl:

                    self.log(
                        "Calling yt-dlp download()"
                    )

                    ydl.download([link])

                self.log(
                    "yt-dlp finished"
                )


            except Exception as error:

                self.log(
                    f"Download exception: {error}"
                )


    def get_options(self, link):

        self.log(
            "Building yt-dlp options"
        )

        options = {

            "outtmpl":
                f"{self.settings.save_path}/%(title)s.%(ext)s",

            "format":
                self.get_quality(),

            "nocheckcertificate":
                self.settings.trust_all_certificates,

            "ignoreerrors":
                True,

            "logger":
                YTDLPLogger(
                    self.progress_manager
                ),

            "verbose":
                True,
        }


        if self.settings.proxy_enabled:

            if self.settings.proxy_type == "http":

                proxy = "http://"

            else:

                proxy = "socks5h://"


            options["proxy"] = (
                f"{proxy}"
                f"{self.settings.proxy_ip}:"
                f"{self.settings.proxy_port}"
            )

            self.log(
                f"Proxy enabled: {proxy}"
            )


        if self.settings.browser_cookies_enabled:

            options["cookiesfrombrowser"] = (
                self.settings.browser,
            )

            self.log(
                f"Browser cookies: {self.settings.browser}"
            )


        if self.is_youtube_url(link):

            options["remote_components"] = [
                "ejs:github"
            ]

            self.log(
                "Enabled YouTube remote components: ejs:github"
            )


        return options


    def get_quality(self):

        if self.settings.download_quality == "low":

            return "worst"


        if self.settings.download_quality == "medium":

            return "best[height<=720]"


        return "best"


    def is_youtube_url(self, url):

        youtube_domains = [
            "youtube.com",
            "www.youtube.com",
            "youtu.be",
        ]

        return any(
            domain in url
            for domain in youtube_domains
        )


    def log(self, message):

        if self.progress_manager:

            self.progress_manager.log(
                message
            )

        else:

            print(message)