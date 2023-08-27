# Twitter Video Downloader _[DEPRECATED]_

⚠️ _Deprecation Notice_ ⚠️

📢 _Attention users of the Twitter Video Downloader tool!_ 📢

_We regret to inform you that the current version of the Twitter Video Downloader, which relies on the TwitterVid.com site, is no longer functional due to recent updates on the TwitterVid.com website._

_As a result, you will no longer be able to use this tool to download videos from Twitter. We understand the convenience this tool brought to your video downloading experience, and we apologize for any inconvenience caused by this discontinuation._

_We recommend exploring alternative solutions to fulfill your Twitter video downloading needs. There are several other tools and scripts available online that might offer similar functionality. However, please ensure that you only use tools that are safe and respect the terms of service of the websites you are downloading content from._

_Thank you for your understanding and for being a user of our Twitter Video Downloader tool. If you have any questions or need assistance in finding alternative solutions, please feel free to reach out to us._

---
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

3. Install the required packages

   ```bash
   pip install -r requirements.txt

4. Run the script with the video URL as the argument

   ```bash
   python twitter_downloader.py {video url}

   eg :- python twitter_downloader.py https://twitter.com/TrollFootball/status/1679583964770754560?s=20

## Note

- This script relies on the external website [TwitterVid.com](https://twittervid.com/) to retrieve the video URL for downloading. It uses the API provided by TwitterVid.com to fetch the video details.
- Please ensure you have a stable internet connection and access to TwitterVid.com for the script to work properly.
- Me and this project are not affiliated with [TwitterVid.com](https://twittervid.com/). Please review and comply with the terms and conditions of [TwitterVid.com](https://twittervid.com/) when using their services through this script.
