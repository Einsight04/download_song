import os
import subprocess
import sys


def download_song(song_name):
    output_folder = "downloaded_songs"
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    output_template = f"{output_folder}/%(title)s.%(ext)s"

    command = [
        "yt-dlp",
        "--no-check-certificate",
        "--extract-audio",
        "--audio-format",
        "mp3",
        "--prefer-ffmpeg",
        "--default-search",
        "ytsearch",
        "--output",
        output_template,
        song_name,
    ]

    try:
        subprocess.run(command, check=True)
        print(f"'{song_name}' downloaded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python download_song.py <song_name>")
        sys.exit(1)

    song_name = " ".join(sys.argv[1:])
    download_song(song_name)
