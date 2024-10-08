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
