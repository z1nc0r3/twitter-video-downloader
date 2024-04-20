# Twitter Video Downloader 2.0

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fz1nc0r3%2Ftwitter-video-downloader&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

---
This is a Python script that allows you to download videos from X aka Twitter using the terminal. It takes a Twitter post URL as an input, extracts the highest-quality video URL, and downloads the video.

## Prerequisites

- Python 3.x
- requests library (install requirements using `pip install requests`)
- bs4 library (install using `pip install beautifulsoup4`)
- tqdm library (install using `pip install tqdm`)

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/z1nc0r3/twitter-video-downloader

2. Navigate to the project directory:

   ```bash
   cd twitter-video-downloader

3. Install the required packages

   ```bash
   pip install -r requirements.txt

4. Run the script with the video URL as the argument

   ```bash
   python twitter_downloader.py {video url}

   eg :- python twitter_downloader.py https://x.com/realmadriden/status/1743790569866821949?s=20

## Note

- This script relies on the external website [twitsave.com](https://twitsave.com) to retrieve the video URL for downloading. It uses the API provided by twitsave.com to fetch the video details.
- Please ensure you have a stable internet connection and access to twitsave.com for the script to work properly.
- Me and this project are not affiliated with [twitsave.com](https://twitsave.com). Please review and comply with the terms and conditions of [twitsave.com/terms](https://twitsave.com/terms) when using their services through this script.
