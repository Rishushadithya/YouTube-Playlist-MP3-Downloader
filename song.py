import yt_dlp
import os

# --- Configuration ---
# ❗️ PASTE YOUR YOUTUBE PLAYLIST URL HERE
PLAYLIST_URL = 'https://www.youtube.com/playlist?list=PLc5WuLipRJJ7nKxY9wsdbEQLGtmYq7Ahm'

# The script will look for a file named 'cookies.txt' in the same folder.
COOKIE_FILE = 'cookies.txt'

# ❗️ SET THE PATH TO YOUR FFMPEG FOLDER HERE
# Use forward slashes (/) instead of backslashes (\)
FFMPEG_PATH = 'C:/ffmpeg'

# Set the download directory name
DOWNLOAD_DIRECTORY = 'Downloaded Songs'
# --- End of Configuration ---


def download_playlist_as_mp3(url, download_path, cookie_file, ffmpeg_loc):
    """
    Downloads a YouTube playlist and converts videos to MP3, using a cookie file.
    """
    if not os.path.exists(download_path):
        os.makedirs(download_path)
        print(f"Created directory: {download_path}")

    # yt-dlp options
    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(title)s'),
        'format': 'bestaudio/best',
        'cookiefile': cookie_file,
        
        # This new option tells the script where ffmpeg.exe is located
        'ffmpeg_location': ffmpeg_loc,

        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ignoreerrors': True,
        'verbose': False, 
    }

    try:
        print(f"👤 Using cookie file: {cookie_file}")
        print(f"🎵 Starting download for playlist: {url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n✅ Download completed successfully!")
        print(f"Files saved in: {os.path.abspath(download_path)}")

    except Exception as e:
        print(f"\n❌ An error occurred: {e}")


if __name__ == '__main__':
    if 'YOUR_PLAYLIST_ID' in PLAYLIST_URL:
        print("❌ Error: Please replace the placeholder URL.")
    elif not os.path.exists(COOKIE_FILE):
        print(f"❌ Error: Could not find the cookie file named '{COOKIE_FILE}'.")
    else:
        download_playlist_as_mp3(PLAYLIST_URL, DOWNLOAD_DIRECTORY, COOKIE_FILE, FFMPEG_PATH)