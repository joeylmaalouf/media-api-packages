import requests

CLIENT_ID = "" # generate your own at https://developer.spotify.com/my-applications
CLIENT_SECRET = "" # generate your own at https://developer.spotify.com/my-applications
TOKEN_URL = "https://accounts.spotify.com/api/token"
TRACKLIST_URL = "https://api.spotify.com/v1/users/{user_id}/playlists/{playlist_id}/tracks"


def get_token(client_id, client_secret):
	response_data = requests.post(TOKEN_URL, data = {"grant_type": "client_credentials"}, auth = (client_id, client_secret)).json()
	return "Authorization: {0} {1}".format(response_data["token_type"], response_data["access_token"])


def get_playlist_tracks(user_id, playlist_id):
	url = TRACKLIST_URL.format(user_id = user_id, playlist_id = playlist_id)
	token_string = get_token(CLIENT_ID, CLIENT_SECRET)
	response = requests.get(url, headers = {"Authorization": token_string})
	for item in response.json()["items"]:
		yield item["track"]["name"].encode("utf-8"), [artist["name"].encode("utf-8") for artist in item["track"]["artists"]]


if __name__ == "__main__":
	for song, artists in get_playlist_tracks("inkdota", "42OR4AZARbwKePmb90SHrA"):
		print("\"{0}\" by {1}".format(song, ", ".join(artists)))
