from textual.widgets import Label, RichLog

from src.ui.screens.base import BaseScreen


class LogsScreen(BaseScreen):

    def screen_content(self):

        yield Label("Application Logs")
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

        # Show existing logs
        for log in self.app.progress_manager.get_logs():

            self.log_widget.write(log)

        # Receive future logs
        self.app.progress_manager.set_log_callback(
            self.add_log
        )

    def add_log(self, message):

        self.log_widget.write(message)