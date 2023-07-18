import sys
import os
import re

import requests

from tqdm import tqdm
from pathlib import Path


def extract_video_id(url) -> None | int:
    """Extract the video ID from a given url

    Args:
        url (str): The URL to extract the video from.

    Returns (None | int): Either an integer if there is a url or None.
    """

    pattern = r"status/(\d+)"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None


def download_video(url, file_name) -> None:
    """Download a video from a URL into a filename.

    Args:
        url (str): The URL to download
        file_name (str): The file name or path to save the video to.
    """

    response = requests.get(url, stream=True)
    total_size = int(response.headers.get("content-length", 0))
    block_size = 1024
    progress_bar = tqdm(total=total_size, unit="B", unit_scale=True)

    download_path = os.path.join(Path.home(), "Downloads", file_name)

    with open(download_path, "wb") as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)

    progress_bar.close()
    print("Video downloaded successfully!")


def download_twitter_video(url, file_name):
    """Extract a video ID to download into a file

    Args:
        url (str): The URL to download from
        file_name (str): The file name to save the video to.
    """

    video_id = extract_video_id(url)
    api_url = f"https://api.twitterpicker.com/tweet/mediav2?id={video_id}"

    response = requests.get(api_url)
    data = response.json()

    videos = data["media"]["videos"][0]["variants"]
    highest_bitrate = max(videos, key=lambda x: int(x.get("bitrate", 0) or 0))
    video_url = highest_bitrate["url"]

    download_video(video_url, file_name)


if len(sys.argv) < 2:
    print('Please provide the Twitter video URL as a command line argument.')
else:
    twitter_video_url = sys.argv[1]
    video_id = extract_video_id(twitter_video_url)
    if video_id:
        file_name = f'{video_id}.mp4'
        download_twitter_video(twitter_video_url, file_name)
    else:
        print('Invalid Twitter video URL provided.')