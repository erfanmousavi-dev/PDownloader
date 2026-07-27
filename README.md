````markdown
# PDownloader

> ⚠️ **Windows Support Notice**
>
> Windows is currently **not officially supported**.
>
> PDownloader may start and the interface may work on Windows, but downloading features can have problems because of differences in SSL certificates, browser cookies, external dependencies, and yt-dlp requirements.
>
> The project is currently developed and tested mainly on Linux and macOS. Windows support will be improved in the future.

---

## About This Project

PDownloader is a terminal-based video and audio downloader that uses **yt-dlp** for downloading and **Textual** for the user interface.

I used AI tools during development to help with repetitive coding tasks, documentation cleanup, and translation. AI is a tool, and I still review, test, and maintain the code myself.

If you notice any mistakes, bad practices, or unnecessary AI-generated code, please let me know politely by opening an issue. Suggestions and improvements are welcome!

---

# Installation

## Requirements

Before installing PDownloader, make sure you have:

* Python installed
* Git installed

You can check by running:

```bash
python --version
````

or:

```bash
python3 --version
```

---

## Step 1: Download the Project

The recommended way is using Git:

```bash
git clone https://github.com/erfanmousavi-dev/PDownloader.git
```

You can also download the ZIP file from GitHub, but using Git is recommended because it makes updating easier.

After downloading, enter the project directory:

```bash
cd PDownloader
```

---

## Step 2: Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv venv
```

Activate it:

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```powershell
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Step 3: Run PDownloader

Start the application:

```bash
python main.py
```

---

# How To Use

## Adding Download Links

1. Open the **Add Links** screen by pressing:

```
2
```

on your keyboard.

2. Paste your download link or links into the input box.

You can add multiple links separated by:

* Space
* Comma (,)

3. Press **Enter** to add the links to your download list.

---

## Downloading Videos

After adding your links:

1. Press the **Download** button.

2. The downloads will start in the background.

3. Open the Home screen:

```
1
```

to see download progress.

---

## YouTube Downloads

For YouTube downloads:

1. Open the **Options** screen:

```
3
```

2. Enable browser cookies.

3. Select the browser where you are logged into YouTube:

* Firefox
* Chrome

4. Return to the Add Links screen.

5. Add your YouTube links and start downloading.

---

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

# Troubleshooting

## Windows Downloads Not Working

Windows support is still experimental.

If downloads fail:

* Make sure Python is installed correctly.
* Use a virtual environment.
* Install all requirements again.
* Make sure yt-dlp dependencies are available.
* Check the application Logs screen for errors.

---

# Contributing

Contributions, bug reports, and suggestions are welcome.

If you find a problem, please open an issue or submit a pull request.

---

# License

This project is open source. Check the repository license for more information.