YouTube Playlist to MP3 Downloader 🎵
This Python script downloads all videos from a YouTube playlist and converts them into high-quality MP3 files. It organizes the downloaded songs into a dedicated folder and can use browser cookies to access age-restricted or private playlists.

Features
Downloads an entire YouTube playlist.

Converts video to MP3 format using FFmpeg.

Saves files in a clean, numbered format: Track Number - Title.mp3.

Supports cookies for authentication on private or age-restricted content.

Installation & Usage
Follow these steps to set up and run the project on your local machine.

1. Clone the Repository
First, get the code by cloning this repository. Open your terminal and run:

Bash

git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
(Replace YOUR_USERNAME and YOUR_REPOSITORY with your actual GitHub details.)

2. Install Dependencies
This project has two main dependencies: a Python library and a command-line tool.

yt-dlp (Python library):

Bash

py -m pip install yt-dlp
FFmpeg (for audio conversion):

Download FFmpeg from this link. (The ...win64-gpl-....zip file is a good choice).

Create a folder named C:\ffmpeg.

Unzip the download, open the bin folder, and copy ffmpeg.exe into C:\ffmpeg.

The script is already configured to look for FFmpeg in this location.

3. Configure the Script
Before running, you need to set up two things inside the song.py file:

Playlist URL: Open song.py and paste the URL of the YouTube playlist you want to download into the PLAYLIST_URL variable.

Cookies (Recommended):

Install a browser extension like "Get cookies.txt LOCALLY".

Go to YouTube and export your cookies.

Save the file as cookies.txt in the same folder as the script.

4. Run the Script
Once everything is set up, run the script from your terminal:

Bash

py song.py
The script will create a Downloaded Songs folder and begin downloading your playlist.
