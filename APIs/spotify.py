import requests


# generate your own at https://developer.spotify.com/my-applications
CLIENT_ID = ""
CLIENT_SECRET = ""


def generate_token_string(client_id, client_secret):
	response = requests.post("https://accounts.spotify.com/api/token",
		data = {"grant_type": "client_credentials"},
		auth = (client_id, client_secret)).json()
	return "Authorization: {0} {1}".format(response["token_type"], response["access_token"])
TOKEN_STRING = generate_token_string(CLIENT_ID, CLIENT_SECRET)


def authorized_get(url, **kwargs):
	return requests.get(url, headers = {"Authorization": TOKEN_STRING}, **kwargs).json()


class Track(object):
	def __init__(self, track_id):
		super(Track, self).__init__()
		response = authorized_get("https://api.spotify.com/v1/tracks/{track_id}".format(track_id = track_id))
		self.id = response["id"]
		self.name = response["name"].encode("utf-8")
		self.artists = [artist["name"].encode("utf-8") for artist in response["artists"]]
		duration = int(response["duration_ms"]) / 1000
		self.length = {"minutes": duration / 60, "seconds": duration % 60}

	def __str__(self):
		return "\"{0}\" - {1} ({2}:{3:02d})".format(
			self.name, ", ".join(self.artists),self.length["minutes"], self.length["seconds"])


class Playlist(object):
	def __init__(self, user_id, playlist_id):
		super(Playlist, self).__init__()
		response = authorized_get("https://api.spotify.com/v1/users/{user_id}/playlists/{playlist_id}".format(
			user_id = user_id, playlist_id = playlist_id))
		self.id = response["id"]
		self.name = response["name"].encode("utf-8")
		self.owner = response["owner"]["id"].encode("utf-8")
		self.tracks = [Track(track["track"]["id"]) for track in response["tracks"]["items"]]

	def __str__(self):
		return "\"{0}\" - {1} ({2} song{3})".format(
			self.name, self.owner, len(self.tracks), "" if len(self.tracks) == 1 else "s")


def get_playlists_from_user(user_id):
	response = authorized_get("https://api.spotify.com/v1/users/{user_id}/playlists".format(user_id = user_id))
	return [Playlist(user_id, playlist["id"]) for playlist in response["items"]]


if __name__ == "__main__":
	for playlist in get_playlists_from_user("inkdota"):
		print("Playlist: {0}".format(playlist))
		for track in playlist.tracks:
			print("\tTrack: {0}".format(track))
		print("")
