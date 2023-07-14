# Twitter Video Downloader

This is a Python script that allows you to download videos from Twitter. It takes a Twitter video URL as input, extracts the video ID, and downloads the video using the URL with the highest bitrate.

## Prerequisites

- Python 3.x
- requests library (install using `pip install requests`)
- tqdm library (install using `pip install tqdm`)

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/twitter-video-downloader.git

2. Navigate to the project directory:

   ```bash
   cd twitter-video-downloader

3. Run the script with the video URL as the argument

   ```bash
   python twitter_downloader.py {video url}

   eg :- python twitter_downloader.py https://twitter.com/TrollFootball/status/1679583964770754560?s=20

## Note

- This script relies on the external website [TwitterVid.com](https://twittervid.com/) to retrieve the video URL for downloading. It uses the API provided by TwitterVid.com to fetch the video details.
- Please ensure you have a stable internet connection and access to TwitterVid.com for the script to work properly.
- Me and this project are not affiliated with [TwitterVid.com](https://twittervid.com/). Please review and comply with the terms and conditions of [TwitterVid.com](https://twittervid.com/) when using their services through this script.
