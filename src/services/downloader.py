import yt_dlp


class Downloader:

    def __init__(self, settings, progress_manager=None):

        self.settings = settings
        self.progress_manager = progress_manager


    def download(self, links):

        for link in links:

            if self.is_youtube_url(link):

                if not self.settings.browser_cookies_enabled:

                    print(
                        "YouTube download skipped: "
                        "Enable browser cookies in settings."
                    )

                    continue


            options = self.get_options(link)

            if self.progress_manager:

                download = (
                    self.progress_manager
                    .create(link)
                )

                options["progress_hooks"] = [
                    self.progress_manager.hook(download)
                ]


            try:

                with yt_dlp.YoutubeDL(options) as ydl:

                    ydl.download([link])


            except Exception as error:

                print(
                    f"Download error: {error}"
                )


    def get_options(self, link):

        options = {

            "outtmpl":
                f"{self.settings.save_path}/%(title)s.%(ext)s",

            "format":
                self.get_quality(),

            "nocheckcertificate":
                self.settings.trust_all_certificates,

            "ignoreerrors":
                True,
        }


        if self.settings.proxy_enabled:

            if self.settings.proxy_type == "http":

                proxy = "http://"

            else:

                proxy = "socks5://"


            options["proxy"] = (
                f"{proxy}"
                f"{self.settings.proxy_ip}:"
                f"{self.settings.proxy_port}"
            )


        if self.settings.browser_cookies_enabled:

            options["cookiesfrombrowser"] = (
                self.settings.browser,
            )


        if self.is_youtube_url(link):

            options["remote_components"] = [
                "ejs:github"
            ]


        return options


    def get_quality(self):

        if self.settings.download_quality == "low":

            return "worst"


        if self.settings.download_quality == "medium":

            return "best[height<=720]"


        return "bestvideo+bestaudio/best"


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