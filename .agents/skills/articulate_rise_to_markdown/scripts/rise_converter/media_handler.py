import urllib.request
import urllib.error
import subprocess
from pathlib import Path

try:
    from youtube_transcript_api import YouTubeTranscriptApi
    has_yta = True
except ImportError:
    has_yta = False

def validate_url(url):
    """Validates that the base URL is reachable before proceeding."""
    test_url = url.rstrip('/') + '/index.html'
    try:
        req = urllib.request.Request(test_url, method="HEAD")
        urllib.request.urlopen(req, timeout=10)
        return True
    except urllib.error.URLError as e:
        print(f"URL Validation Failed for {test_url}: {e}")
        return False

def download_file(url, output_path):
    """Downloads a file from a URL to the specified local path."""
    try:
        urllib.request.urlretrieve(url, output_path)
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False

def extract_youtube_id(url):
    """Extracts the video ID from standard YouTube URLs."""
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    return None

def fetch_youtube_transcript(video_id):
    """Fetches the transcript text using youtube-transcript-api."""
    if not has_yta:
        raise ImportError("youtube-transcript-api is not installed.")
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([t['text'] for t in transcript])
    except (AttributeError, TypeError):
        ytt = YouTubeTranscriptApi()
        res = ytt.fetch(video_id)
        return " ".join([s.text for s in res.snippets])

def download_video_yt_dlp(url, output_path):
    """Downloads a YouTube video using yt-dlp via subprocess."""
    subprocess.run(['yt-dlp', '-f', 'worst', '-o', str(output_path), url], check=True, capture_output=True)
