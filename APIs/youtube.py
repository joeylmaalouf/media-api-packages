from pytube import YouTube
import re
import requests


def search(query):
	response = requests.get("https://www.youtube.com/results?search_query={}".format(query))
	matches = re.findall("<h3.*<a href.+</a><span.+</span></h3>", response.content)
	for match in matches:
		if "Duration" in match: # make sure it's a video, not a playlist
			video_id = re.search("v=[-,_,a-z,A-Z,0-9,]+", match).group(0)[2:]
			yield Video(video_id)


def download(video_url_or_id, folder_path = "./"):
	if "youtube.com" in video_url_or_id:
		video_id = video_url_or_id.split("v=")[-1]
	elif "youtu.be" in video_url_or_id:
		video_id = video_url_or_id.split(".be/")[-1]
	else:
		video_id = video_url_or_id
	video_id = re.search("[\w-]+", video_id).group(0)

	yt = YouTube()
	yt.from_url("http://www.youtube.com/watch?v={}".format(video_id))
	yt.filter("mp4")[-1].download(path = folder_path, force_overwrite = True)


class Video(object):
	def __init__(self, video_id):
		super(Video, self).__init__()
		self.id = video_id
		response = requests.get("https://www.youtube.com/watch?v={}".format(video_id))
		self.title = re.search(">.*<", re.search("<span id=\"eow-title\"(.*?)</span>", response.content, re.DOTALL).group(0), re.DOTALL).group(0)[6:-4]
		self.channel = re.search(" >.*<", re.search("<div class=\"yt-user-info(.*?)</a>", response.content, re.DOTALL).group(0), re.DOTALL).group(0)[2:-1]

	def __str__(self):
		return "Video: \"{0}\" - {1}".format(self.title, self.channel)

	def download(self, folder_path = "./"):
		download(self.id, folder_path)


if __name__ == "__main__":
	for result in search("Megadeth - A Tout Le Monde"):
		print(result)

	v = Video("dQw4w9WgXcQ")
	v.download()
