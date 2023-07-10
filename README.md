pytube library to download videos from YouTube. It provides two functions: download_video() and download_playlist().

The download_video() function takes a YouTube video URL as input, creates a YouTube object using the URL, and retrieves the highest resolution video stream available. It then downloads the video using the download() method of the stream object. If any exception occurs during the process, an error message is printed.

The download_playlist() function takes a YouTube playlist URL as input, creates a Playlist object using the URL, and prints the total number of videos in the playlist. It then iterates over each video URL in the playlist and calls the download_video() function to download each video.

The main program prompts the user to enter a YouTube video URL or playlist URL. It checks if the input contains the string "youtube.com/playlist" to determine whether it is a playlist URL or a video URL. If it's a playlist URL, the download_playlist() function is called with the input URL. Otherwise, the download_video() function is called.

In summary, this code allows the user to download either a single YouTube video or a playlist of videos by entering the corresponding URL.
