from textual.widgets import (Label, Input, Checkbox, Select, Button)

from src.ui.screens.base import BaseScreen


class OptionsScreen(BaseScreen):

    def __init__(self, settings):

        super().__init__()

        self.settings = settings

    def screen_content(self):

        yield Label("\n")
        yield Label("Options Screen")
        yield Label("\n")

        yield Label("Save Path")
        yield Input(
            value=self.settings.save_path,
            id="save_path"
        )

        yield Label("\n")

        yield Checkbox(
            "Enable Proxy",
            value=self.settings.proxy_enabled,
            id="proxy_enabled"
        )

        yield Label("\n")

        yield Label("Proxy Type")
        yield Select(
            [
                ("HTTP", "http"),
                ("SOCKS", "socks"),
            ],
            value=self.settings.proxy_type,
            id="proxy_type"
        )

        yield Label("\n")

        yield Label("Proxy IP")
        yield Input(
            value=self.settings.proxy_ip,
            id="proxy_ip"
        )

        yield Label("\n")

        yield Label("Proxy Port")
        yield Input(
            value=self.settings.proxy_port,
            id="proxy_port"
        )

        yield Label("\n")

        yield Label("Download Quality")
        yield Select(
            [
                ("Low", "low"),
                ("Medium", "medium"),
                ("High", "high"),
            ],
            value=self.settings.download_quality,
            id="download_quality"
        )

        yield Label("\n")

        yield Checkbox(
            "Trust all certificates",
            value=self.settings.trust_all_certificates,
            id="trust_certificates"
        )

        yield Label("\n")

        yield Label("Browser Cookies")

        yield Checkbox(
            "Enable browser cookies",
            value=self.settings.browser_cookies_enabled,
            id="browser_cookies_enabled"
        )

        yield Label("\n")

        yield Label("Browser")

        yield Select(
            [
                ("Firefox", "firefox"),
                ("Chrome", "chrome"),
            ],
            value=self.settings.browser,
            id="browser"
        )

        yield Label("\n")

        yield Button(
            "Save Settings",
            id="save_settings"
        )


    def on_button_pressed(self, event: Button.Pressed):

        if event.button.id == "save_settings":

            self.save_settings()


    def save_settings(self):

        self.settings.save_path = (
            self.query_one("#save_path").value
        )

        self.settings.proxy_enabled = (
            self.query_one("#proxy_enabled").value
        )

        self.settings.proxy_type = (
            self.query_one("#proxy_type").value
        )

        self.settings.proxy_ip = (
            self.query_one("#proxy_ip").value
        )

        self.settings.proxy_port = (
            self.query_one("#proxy_port").value
        )

        self.settings.download_quality = (
            self.query_one("#download_quality").value
        )

        self.settings.trust_all_certificates = (
            self.query_one("#trust_certificates").value
        )

        self.settings.browser_cookies_enabled = (
            self.query_one("#browser_cookies_enabled").value
        )

        self.settings.browser = (
            self.query_one("#browser").value
        )

        self.settings.save()

        self.app.notify("Settings saved")