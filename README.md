# Media Packages

Contains a number of my different media-related Python interfaces, as well as examples showing how to use and combine them.


## YouTube
#####(`APIs/youtube.py`)

function `search`: Given a search query, return one page's worth of YouTube search results, specifically the video IDs, titles, and durations.

function `download`: Given a video ID or URL, and an optional directory path (defaults to current directory), download the video to the directory (as a highest-quality .mp4).


## Spotify
#####(`APIs/spotify.py`)

function `generate_token_string`: Using the per-app-generated CLIENT_ID and CLIENT_SECRET (https://developer.spotify.com/my-applications), generate an authentication token string.

function `authorized_get`:  Using the TOKEN_STRING, perform an authorized GET on the given URL.

function `get_playlists_from_user`: Given a user ID, return all of their playlists as Playlists objects containing Track objects.

class `Playlist`: Given a user ID and a playlist ID, collect all of the playlist's relevant data in an object.

class `Track`: Given a track ID, collect all of the given track's relevant data in an object.


## Example Usage
#####(`projects/spotify-playlist-downloader.py`)

```python
from APIs import youtube, spotify

user_id = ...
playlist_id = ...

for track in spotify.Playlist(user_id, playlist_id).tracks:
	query = "{0} - {1}".format(track.name, ", ".join(track.artists))
	video_id = next(youtube.search(query))["id"]
	youtube.download(video_id, path)
```
