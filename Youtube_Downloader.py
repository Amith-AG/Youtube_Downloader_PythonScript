from pytube import YouTube, Playlist

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
user_input = input("Enter YouTube video URL or playlist URL: ")
if "youtube.com/playlist" in user_input:
    download_playlist(user_input)
else:
    download_video(user_input)
