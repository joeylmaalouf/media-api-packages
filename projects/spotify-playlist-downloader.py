import os, sys
sys.path.append("..")
from APIs import youtube, spotify


if __name__ == "__main__":
	if len(sys.argv) not in [3, 4]:
		print("Usage: {} <spotify user_id> <spotify playlist_id> [output_directory (defaults to ./)]".format(sys.argv[0].split("/")[-1]))
		sys.exit(1)

	filename, user_id, playlist_id = sys.argv[:3]
	path = sys.argv[3] if len(sys.argv) == 4 else "./"

	if not os.path.isdir(path):
		print("Creating path \"{}\"".format(path))
		os.makedirs(path)

	for track in spotify.Playlist(user_id, playlist_id).tracks:
		query = "{0} - {1}".format(track.name, ", ".join(track.artists))
		video_id = next(youtube.search(query))["id"]
		youtube.download(video_id, path)
