import json
from pathlib import Path
import sys

class Settings:

    def __init__(self):

        if getattr(sys, "frozen", False):
            base_dir = Path(sys.executable).parent
        else:
            base_dir = Path(__file__).resolve().parents[2]

        downloads_path = base_dir / "downloads"
        downloads_path.mkdir(parents=True, exist_ok=True)

        self.file_path = base_dir / "settings.json"
        self.save_path = base_dir / "downloads"
        self.proxy_enabled = False
        self.proxy_type = "socks"
        self.proxy_ip = ""
        self.proxy_port = ""
        self.download_quality = "high"
        self.trust_all_certificates = False

        self.browser_cookies_enabled = False
        self.browser = "firefox"

        self.load()

    def load(self):

        if not self.file_path.exists():

            self.save()
            return

        with open(self.file_path, "r") as file:

            data = json.load(file)

        self.save_path = data.get("save_path", self.save_path)
        self.proxy_enabled = data.get("proxy_enabled", self.proxy_enabled)
        self.proxy_type = data.get("proxy_type", self.proxy_type)
        self.proxy_ip = data.get("proxy_ip", self.proxy_ip)
        self.proxy_port = data.get("proxy_port", self.proxy_port)
        self.download_quality = data.get("download_quality", self.download_quality)
        self.trust_all_certificates = data.get(
            "trust_all_certificates",
            self.trust_all_certificates,
        )

        self.browser_cookies_enabled = data.get(
            "browser_cookies_enabled",
            self.browser_cookies_enabled,
        )

        self.browser = data.get(
            "browser",
            self.browser,
        )

    def save(self):

        data = {
            "save_path": self.save_path,
            "proxy_enabled": self.proxy_enabled,
            "proxy_type": self.proxy_type,
            "proxy_ip": self.proxy_ip,
            "proxy_port": self.proxy_port,
            "download_quality": self.download_quality,
            "trust_all_certificates": self.trust_all_certificates,
            "browser_cookies_enabled": self.browser_cookies_enabled,
            "browser": self.browser,
        }

        with open(self.file_path, "w") as file:

            json.dump(data, file, indent=4)