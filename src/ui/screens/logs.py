import sys
from pathlib import Path

from datetime import datetime

from textual.widgets import Label, RichLog, Button

from src.ui.screens.base import BaseScreen


class LogsScreen(BaseScreen):

    def screen_content(self):

        yield Label("Application Logs")

        yield Button(
            "Save Logs",
            id="save_logs",
        )

        yield RichLog(
            id="logs",
            wrap=True,
            highlight=True,
            markup=False,
        )


    def on_mount(self):

        self.log_widget = self.query_one(
            "#logs",
            RichLog,
        )

        for log in self.app.progress_manager.get_logs():

            self.log_widget.write(log)


        self.app.progress_manager.set_log_callback(
            self.add_log
        )


    def add_log(self, message):

        self.log_widget.write(message)


    def on_button_pressed(self, event: Button.Pressed):

        if event.button.id == "save_logs":

            self.save_logs()


    def save_logs(self):

        if getattr(sys, "frozen", False):
            base_dir = Path(sys.executable).parent
        else:
            base_dir = Path(__file__).resolve().parents[3]

        logs_path = base_dir / "logs"
        logs_path.mkdir(parents=True, exist_ok=True)
    
        logs = self.app.progress_manager.get_logs()

        if not logs:

            self.app.notify(
                "No logs to save"
            )

            return


        filename = (
            "pdownloader_log_"
            f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
            ".txt"
        )

        save_path = logs_path / filename

        with open(
            save_path,
            "w",
            encoding="utf-8",
        ) as file:

            file.write(
                "\n".join(logs)
            )


        self.app.notify(
            f"Logs saved: {filename}"
        )