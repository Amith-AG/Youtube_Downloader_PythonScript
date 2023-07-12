from pytube import YouTube, Playlist, extract

# Function to download a single video
def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        print(f"Downloading video: {yt.title}")
        stream.download()
        print("Download completed!")
    except Exception as e:
        print(f"Error: {str(e)}")

# Function to download a single audio
def download_audio(url):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        print(f"Downloading audio: {yt.title}")
        audio_stream.download()
        print("Download completed!")
    except Exception as e:
        print(f"Error: {str(e)}")

# Function to download a playlist
def download_playlist(url):
    try:
        playlist = Playlist(url)
        print(f"Total videos in playlist: {len(playlist.video_urls)}")
        for video_url in playlist.video_urls:
            download_video(video_url)
    except Exception as e:
        print(f"Error: {str(e)}")

# Main program
print("Select an option:")
print("1. Download a video")
print("2. Download audio")
print("3. Download a playlist")

user_option = input("Enter your choice (1, 2, or 3): ")
user_url = input("Enter YouTube video URL or playlist URL: ")

if user_option == "1":
    download_video(user_url)
elif user_option == "2":
    download_audio(user_url)
elif user_option == "3" and "youtube.com/playlist" in user_url:
    download_playlist(user_url)
else:
    print("Invalid option or URL.")