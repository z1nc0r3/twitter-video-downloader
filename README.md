# Twitter Video Downloader

---
This is a Python script that allows you to download videos from X aka Twitter using terminal. It takes a Twitter post URL as input, extracts the highest quality video url, and downloads the video.

## Prerequisites

- Python 3.x
- requests library (install requirements using `pip install requests`)
- bs4 library (install using `pip install beautifulsoup4`)
- tqdm library (install using `pip install tqdm`)

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/twitter-video-downloader.git

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
