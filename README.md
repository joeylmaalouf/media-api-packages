# Media Packages

Contains a number of my different media-related Python interfaces, as well as examples showing how to use and combine them.


## YouTube

`search`: Given a search query, return one page's worth of YouTube search results, specifically the video IDs, titles, and durations.

`download`: Given a video ID or URL, and an optional directory path (defaults to current directory), download the video to the directory (as a highest-quality .mp4).


## Spotify

`get_token`: Given a client ID and a client secret, return an authentication token string.

`get_playlist_tracks`: Given a user ID and a playlist ID, return all of the song titles (and corresponding artists) in the track list.
