# Moj Video Downloader Bot

A Telegram bot that allows users to download videos from the Moj app using `yt-dlp` and process them with `ffmpeg`. The bot offers a user-friendly interface and seamless experience for video downloading and processing.

## Features

- Download videos from the Moj app using a shareable link.
- Process videos using `ffmpeg` for error correction.
- Share a temporary hosted link for the final output video.
- User-friendly options for interaction.

## Project Structure
moj_video_downloader/
│
├── main.py                   # Main bot code
├── requirements.txt          # List of dependencies
├── .env                      # Environment variables (not included in version control)
├── README.md                 # Project documentation
├── video_processing/          # Directory for processing videos
│   ├── __init__.py           # Makes this a package
│   ├── download.py           # Functions related to downloading videos
│   └── processing.py         # Functions related to video processing
└── utils/                    # Utility functions
    ├── __init__.py           # Makes this a package
    ├── logger.py             # Logging utilities
    └── progress.py           # Progress tracking functions


### Prerequisites

- **Python**: Ensure you have Python 3.8 or higher installed on your machine. You can download it from the [official Python website](https://www.python.org/downloads/).
- **FFmpeg**: This bot requires `ffmpeg` for video processing. Install it according to your operating system:
  - **Windows**: Download the executable from the [FFmpeg website](https://ffmpeg.org/download.html#build-windows) and add it to your system's PATH.
  - **macOS**: Use Homebrew to install `ffmpeg`:
    ```bash
    brew install ffmpeg
    ```
  - **Linux**: Install `ffmpeg` using your package manager:
    ```bash
    sudo apt-get install ffmpeg  # Debian/Ubuntu
    sudo dnf install ffmpeg      # Fedora
    ```

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/moj_video_downloader.git
   cd moj_video_downloader




Here’s an expanded `README.md` that provides detailed instructions and information about your Moj Video Downloader bot. Additionally, I'll explain why `ffmpeg` is not listed in `requirements.txt` and how to install it.

### Updated `requirements.txt`

Since `ffmpeg` is generally not a Python package that can be installed via `pip`, you should not include it in `requirements.txt`. Instead, it must be installed on the server or local environment separately. Here’s the final `requirements.txt` without `ffmpeg`:

```plaintext
Flask==2.2.2
python-telegram-bot==20.3
yt-dlp==2023.1
tqdm==4.66.4
```

### Detailed `README.md`

```markdown
# Moj Video Downloader Bot

## Overview

The Moj Video Downloader Bot is a Telegram bot that allows users to download videos from the Moj app using shareable links. The bot utilizes `yt-dlp` for downloading videos and `ffmpeg` for video processing, including error correction and adjustments to the video file. This bot aims to provide a user-friendly interface and a seamless experience for
## Features

- **Download Videos**: Easily download videos from the Moj app by sharing the video link.
- **Video Processing**: Automatically process downloaded videos using `ffmpeg` for error correction and adjustments.
- **Temporary Hosting**: Generate a temporary hosted link for the processed video to avoid overloading the server.
- **User-Friendly Interface**: An intuitive interface for users to interact with the bot.


## Installation

### Prerequisites

- **Python**: Ensure you have Python 3.8 or higher installed on your machine. You can download it from the [official Python website](https://www.python.org/downloads/).
- **FFmpeg**: This bot requires `ffmpeg` for video processing. Install it according to your operating system:
  - **Windows**: Download the executable from the [FFmpeg website](https://ffmpeg.org/download.html#build-windows) and add it to your system's PATH.
  - **macOS**: Use Homebrew to install `ffmpeg`:
    ```bash
    brew install ffmpeg
    ```
  - **Linux**: Install `ffmpeg` using your package manager:
    ```bash
    sudo apt-get install ffmpeg  # Debian/Ubuntu
    sudo dnf install ff### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/moj_video_downloader.git
   cd moj_video_downloader
   ```

2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required Python packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file in the root directory** and add your Telegram bot token:
   ```plaintext
   BOT_TOKEN=your_bot_token_here
   ```

## Usage

1. **Start the bot**:
   ```bash
   python main.py
   ```

2. **Open Telegram and find your bot** using its username.
3. **Send a link** from the Moj app to the bot to download the video. The bot will process the video and send you a temporary link to access the final output.

## Deployment

### Deploying on Replit

1. **Create a new Replit project**.
2. **Add your code** into the `main.py` file.
3. **Create a `requirements.txt` file** with the dependencies listed above.
4. **Set the `BOT_TOKEN`** in the Secrets section.
5. **Click the "Run" button** to start the bot.

### Deploying on Render

1. **Create a new web service** on Render.
2. **Connect your GitHub repository** to the service.
3. **Set the build command** to install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. **Set the start command** for your bot:
   ```bash
   gunicorn -w 4 -k gthread -b 0.0.0.0:8080 main:app
   ```
5. **Add environment variables** for the bot token in the Render dashboard.

## Logging

The bot logs its activity to help with debugging and monitoring. You can view logs to track errors, downloads, and other important events.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request if you'd like to contribute. 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for video downloading capabilities.
- [FFmpeg](https://ffmpeg.org/) for video processing functionalities.
```

### Final Notes

- Make sure to replace `yourusername` in the clone URL and `your_bot_token_here` with your actual GitHub username and Telegram bot token.
- This `README.md` provides comprehensive information that will help other users understand the project, how to set it up, and how to contribute.
- Customize the document as needed based on any additional features or specific instructions relevant to your project.
