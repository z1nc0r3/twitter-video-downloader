import requests
import re
from tqdm import tqdm

def extract_video_id(url):
    pattern = r"status/(\d+)"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None

def download_video(url, file_name):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024
    progress_bar = tqdm(total=total_size, unit='B', unit_scale=True)

    with open(file_name, 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)

    progress_bar.close()
    print('Video downloaded successfully!')

def download_twitter_video(url, file_name):
    video_id = extract_video_id(url)
    print(video_id)
    api_url = f'https://api.twitterpicker.com/tweet/mediav2?id={video_id}'

    response = requests.get(api_url)
    data = response.json()
    
    videos = data['media']['videos'][0]['variants']
    highest_bitrate = max(videos, key=lambda x: int(x.get('bitrate', 0) or 0))
    video_url = highest_bitrate['url']

    download_video(video_url, file_name)

twitter_video_url = input('Enter Twitter video URL: ')
video_id = extract_video_id(twitter_video_url)
file_name = f'{video_id}.mp4'
download_twitter_video(twitter_video_url, file_name)