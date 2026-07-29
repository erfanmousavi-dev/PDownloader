## About This Project

PDownloader is a terminal-based video and audio downloader that uses **yt-dlp** for downloading and **Textual** for the user interface.

I used **AI** tools during development to help with repetitive coding tasks, documentation cleanup, and translation. AI is a tool, and I still review, test, and maintain the code myself.

If you notice any mistakes, bad practices, or unnecessary AI-generated code, please let me know politely by opening an issue. Suggestions and improvements are welcome!

---

# Installation

There are two ways to use **PDownloader**:

1. **Download the source code** and run it with Python.
2. **Download a pre-built executable** from the GitHub Releases page for your operating system.

# Notice

If you use the pre-built executable, your operating system or antivirus may warn that it could be unsafe. This is because the application is not digitally signed by a certified developer. If you downloaded it from the official GitHub Releases page, you can safely choose **Run Anyway** (or the equivalent option on your operating system).

If you prefer to run the application from source, follow these steps:

```bash
git clone https://github.com/erfanmousavi-dev/PDownloader.git
```

```bash
cd PDownloader
```

```bash
python -m venv venv
```

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows (PowerShell)

```powershell
venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```


# Features

Currently supported features:

* Video and audio downloads using yt-dlp
* Terminal user interface using Textual
* Multiple download links
* Custom download location
* Download quality selection
* Proxy support
* Browser cookie support
* Download progress display
* Application logs for debugging

---

# Supported Websites

PDownloader uses **yt-dlp**, so it supports many websites.

I have tested:

* YouTube
* SoundCloud
* Other websites supported by yt-dlp

If a website does not work, please open an issue with:

* Website URL
* Error message from the logs
* Your operating system

and I will try to investigate the problem.

---

# Settings

You can configure settings from the Options screen, including:

* Download folder
* Download quality
* Proxy settings
* Browser cookie settings
* Certificate verification options

---

# Contributing

Contributions, bug reports, and suggestions are welcome.

If you find a problem, please open an issue or submit a pull request.

---

# License

This project is open source. Check the repository license for more information.