import os
import subprocess


class SongManager:
    def __init__(self):
        self.output_folder = "downloaded_songs"
        if not os.path.exists(self.output_folder):
            os.mkdir(self.output_folder)

    def download_song(self, song_name):
        output_template = f"{self.output_folder}/%(title)s.%(ext)s"

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

    def view_songs(self):
        songs = os.listdir(self.output_folder)
        if not songs:
            print("No downloaded songs found.")
            return

        self._print_songs_with_numbers(songs)

    def delete_song(self):
        songs = os.listdir(self.output_folder)
        if not songs:
            print("No downloaded songs found.")
            return

        self._print_songs_with_numbers(songs)

        try:
            choice = int(input("Enter the number of the song you want to delete: "))
            if 1 <= choice <= len(songs):
                os.remove(os.path.join(self.output_folder, songs[choice - 1]))
                print(f"Deleted '{songs[choice - 1]}'.")
            else:
                print("Invalid choice. No song deleted.")
        except ValueError:
            print("Invalid input. No song deleted.")

    def _print_songs_with_numbers(self, songs):
        lre = "\u202A"  # Left-to-Right Embedding control character
        pdf = "\u202C"  # Pop Directional Formatting control character

        print("Songs:")
        for index, song in enumerate(songs, start=1):
            print(f"{lre}{index}. {song}{pdf}")


def main():
    song_manager = SongManager()

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
                song_manager.download_song(song_name)
            elif choice == 2:
                song_manager.view_songs()
            elif choice == 3:
                song_manager.delete_song()
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
