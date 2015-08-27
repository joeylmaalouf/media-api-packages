import os, sys
sys.path.append("..")
from APIs import youtube, spotify


if __name__ == "__main__":
	# assert proper usage
	if len(sys.argv) not in [3, 4]:
		print("Usage: {} <spotify user_id> <spotify playlist_id> [output_directory (defaults to ./)]".format(sys.argv[0].split("/")[-1]))
		sys.exit(1)

	# assign args to variables
	this, user_id, playlist_id = sys.argv[:3]
	path = sys.argv[3] if len(sys.argv) == 4 else "./"

	# make the given path if it doesn't exist
	if not os.path.isdir(path):
		print("Creating path \"{}\"".format(path))
		os.makedirs(path)

	# authorize the application to access the Spotify Web API
	# generate your own at https://developer.spotify.com/my-applications
	client_id = ""
	client_secret = ""
	spotify.authorize(client_id, client_secret)

	# get each track in the given playlist,
	# search for it on youtube,
	# and download the first result
	for track in spotify.Playlist(user_id, playlist_id).tracks:
		query = "{0} - {1}".format(track.name, ", ".join(track.artists))
		video = youtube.search(query).next()
		video.download(path)
