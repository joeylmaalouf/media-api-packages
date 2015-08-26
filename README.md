# Media Packages

Contains a number of my different media-related Python interfaces, as well as examples showing how to use and combine them.


## YouTube
#####(`APIs/youtube.py`)

`search`: Given a search query, return one page's worth of YouTube search results, specifically the video IDs, titles, and durations.

`download`: Given a video ID or URL, and an optional directory path (defaults to current directory), download the video to the directory (as a highest-quality .mp4).


## Spotify
#####(`APIs/spotify.py`)

`get_token`: Given a client ID and a client secret, return an authentication token string.

`get_playlist_tracks`: Given a user ID and a playlist ID, return all of the song titles (and corresponding artists) in the track list.


## Example Usage
#####(`spotify-playlist-downloader.py`)
```python
for song, artists in spotify.get_playlist_tracks(user_id, playlist_id):
	query = "\"{0}\" by {1}".format(song, ", ".join(artists))
	video_id = next(youtube.search(query))["id"]
	youtube.download(video_id, path)
```
