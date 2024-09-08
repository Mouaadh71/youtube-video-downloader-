#download yt_dlp by typing pip install yt_dlp in the tirminal

import os
import yt_dlp

def download_video(url, resolution, location):
    ydl_opts = {
        'format': f'best[height<={resolution}]',
        'outtmpl': f'{location}/%(title)s.%(ext)s',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    link = input("Enter the link of the video that you want to download: ")
    resolution = input("Enter the maximum resolution you want (e.g., 360, 720, 1080): ").strip()
    location = input("Enter the location where you want to save the video: ").strip()

    if not os.path.exists(location):
        print(f"The specified directory {location} does not exist.")
    else:
        download_video(link, resolution, location)
