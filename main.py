import concurrent.futures
from scripts.extract_videos import download_video_audio
from scripts.transcribe_videos import video_transcribe
from scripts.store_transcriptions import update_transcription
from scripts.upsert_transcription import upsert


urls = [
    'https://youtu.be/xN1-2p06Urc?si=dbxBktksL-AyZSqm',
]

def process_url(url):
    # Download the video and audio
    video_title = download_video_audio(url)
    print(f"Processing video: {video_title}")
    
    # Transcribe the video
    video_transcribe(url , video_title)

    # Update the transcription
    update_transcription(video_title)

    # Upsert the transcription to Google Sheets
    upsert(video_title)

# # Use a ThreadPoolExecutor to download, transcribe and rename the videos in parallel
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     executor.map(process_url, urls)

process_url(urls[0])