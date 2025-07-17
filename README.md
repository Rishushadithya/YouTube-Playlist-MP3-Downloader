**YouTube Playlist to MP3 Downloader** 🎵

This Python script downloads all video from a YouTube playlist and converts them into high-quality MP3 files. It organizes the downloaded songs into a dedicated folder and can use browser cookies to access age-restricted or private playlists.

Features
Downloads an entire YouTube playlist.
Converts video to MP3 format using FFmpeg.
Saves files in a clean, numbered format: Title.mp3.
Supports using a cookies.txt file for authentication on private or age-restricted content.

Installation & Usage

Follow these steps to set up and run the project on your local machine.



1. Clone the Repository

   First, get the code by cloning this repository. Open your terminal and run:

        git clone https://github.com/Rishushadithya/YouTube-Playlist-MP3-Downloader.git

        cd YouTube-Playlist-MP3-Downloader




2. Install Dependencies

This project has two main dependencies: a Python library and a command-line tool.

yt-dlp (Python library):

    py -m pip install yt-dlp


FFmpeg (for audio conversion):

1.Download FFmpeg from this [link](https://github.com/BtbN/FFmpeg-Builds/releases)
 
 (The ffmpeg-n7.1-latest-win64-gpl-7.1.zip file is a good choice.)
 

Create a folder named **C:\ffmpeg** .

Unzip the download, open the bin folder, and copy ffplay.exe , ffmpeg.exe and ffprobe.exe into **C:\ffmpeg** .

The script is already configured to look for FFmpeg in this location.



3. Configure the Script
   
Before running, you need to set up the script.
Add Playlist URL: Open the **song.py** file and paste the URL of the YouTube playlist you want to download into the **PLAYLIST_URL** variable.


Set Up Cookies : Using cookies helps access age-restricted or private content.

A. Install the Extension: 🌐 Open your browser (Chrome, Edge, etc.) and go to its web store. Search for the extension **"Get cookies.txt LOCALLY"** and click "Add to browser" to install it.

B. Export Cookies: Go to the [YouTube](https://www.youtube.com) home page in your browser, click the newly installed extension's icon, and export the cookies.

C. Save the File: Save the exported file with the exact name **cookies.txt** in the same folder as the **song.py** script.



4. Run the Script

Once everything is set up, run the script from your terminal:

bash
    
    py song.py


The script will create a Downloaded Songs folder and begin downloading your playlist.
