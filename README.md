# Media Packages

Contains a number of my different media-related Python interfaces, as well as examples showing how to use and combine them.


## Spotify
#####(`APIs/spotify.py`)

function `authorize`: Using a client ID and client secret (generate yours [here](https://developer.spotify.com/my-applications)), authorize your application to make requests of the Spotify Web API.

function `authorized_get`: Perform an authorized GET on the given URL.

function `get_playlists_from_user`: Given a user ID, return all of their playlists as Playlists objects containing Track objects.

class `Playlist`: Given a user ID and a playlist ID, collect all of the playlist's relevant data in an object.

class `Track`: Given a track ID, collect all of the given track's relevant data in an object.


## VLC
#####(`APIs/vlc.py`)

function `mp4tomp3`: Converts the video file at the given input file path to an audio file and saves it with a different extension in the same place unless given a different output file path.


## YouTube
#####(`APIs/youtube.py`)

function `search`: Given a search query, yield one page's worth of YouTube search results as Video objects.

function `download`: Given a video ID or URL, and an optional directory path (defaults to current directory), download the video to the directory (as a highest-quality .mp4).

class `Video`: Given a video ID, collect all of the given video's relevant data in an object.


## Example Usage
#####(`projects/spotify-playlist-downloader.py`)

```python
from APIs import youtube, spotify

# generate your own at https://developer.spotify.com/my-applications
client_id = ...
client_secret = ...
spotify.authorize(client_id, client_secret)

user_id = ...
playlist_id = ...
path = ...

for track in spotify.Playlist(user_id, playlist_id).tracks:
	query = "{0} - {1}".format(track.name, ", ".join(track.artists))
	video = youtube.search(query).next()
	video.download(path)
```
