import os
import subprocess


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


def delete_song():
    output_folder = "downloaded_songs"
    if not os.path.exists(output_folder):
        print("No downloaded songs found.")
        return

    songs = os.listdir(output_folder)
    if not songs:
        print("No downloaded songs found.")
        return

    print("Downloaded songs:")
    for index, song in enumerate(songs, start=1):
        print(f"{index}. {song}")

    try:
        choice = int(input("Enter the number of the song you want to delete: "))
        if 1 <= choice <= len(songs):
            os.remove(os.path.join(output_folder, songs[choice - 1]))
            print(f"Deleted '{songs[choice - 1]}'.")
        else:
            print("Invalid choice. No song deleted.")
    except ValueError:
        print("Invalid input. No song deleted.")


def view_songs():
    output_folder = "downloaded_songs"
    if not os.path.exists(output_folder):
        print("No downloaded songs found.")
        return

    songs = os.listdir(output_folder)
    if not songs:
        print("No downloaded songs found.")
        return

    print("Downloaded songs:")
    for index, song in enumerate(songs, start=1):
        print(f"{index}. {song}")


def main():
    while True:
        print("\nOptions:")
        print("1. Download a song")
        print("2. View downloaded songs")
        print("3. Delete a downloaded song")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                song_name = input("Enter the name of the song you want to download: ")
                download_song(song_name)
            elif choice == 2:
                view_songs()
            elif choice == 3:
                delete_song()
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
