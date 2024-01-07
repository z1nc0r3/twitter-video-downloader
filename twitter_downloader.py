import sys
import os
import re

import requests
import bs4

from tqdm import tqdm
from pathlib import Path


def download_video(url, file_name) -> None:
    """Download a video from a URL into a filename.

    Args:
        url (str): The video URL to download
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


def download_twitter_video(url):
    """Extract the highest quality video url to download into a file

    Args:
        url (str): The twitter post URL to download from
    """

    api_url = f"https://twitsave.com/info?url={url}"

    response = requests.get(api_url)
    data = bs4.BeautifulSoup(response.text, "html.parser")
    download_button = data.find_all("div", class_="origin-top-right")[0]
    quality_buttons = download_button.find_all("a")
    highest_quality_url = quality_buttons[0].get("href") # Highest quality video url
    
    file_name = data.find_all("div", class_="leading-tight")[0].find_all("p", class_="m-2")[0].text # Video file name
    file_name = re.sub(r"[^a-zA-Z0-9]+", ' ', file_name).strip() + ".mp4" # Remove special characters from file name
    
    download_video(highest_quality_url, file_name)


if len(sys.argv) < 2:
    print("Please provide the Twitter video URL as a command line argument.\nEg: python twitter_downloader.py <URL>")
else:
    url = sys.argv[1]
    if url:
        download_twitter_video(url)
    else:
        print("Invalid Twitter video URL provided.")
