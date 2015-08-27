from pytube import YouTube
import re
import requests


def search(query):
	response = requests.get("https://www.youtube.com/results?search_query={}".format(query))
	matches = re.findall("<h3.*<a href.+</a><span.+</span></h3>", response.content)
	results = []
	for match in matches:
		if "Duration" in match: # make sure it's a video, not a playlist
			video_id = re.search("v=[-,_,a-z,A-Z,0-9,]+", match).group(0)[2:]
			video_title = re.search("ltr\">.+</a>", match).group(0)[5:-4]
			video_duration = re.search("Duration:.*[.]", match).group(0)[10:-1]
			results.append({"id": video_id, "title": video_title, "duration": video_duration})
	return results


def download(video_url, folder_path = "./"):
	if "youtube.com" in video_url:
		video_id = video_url.split("v=")[-1]
	elif "youtu.be" in video_url:
		video_id = video_url.split(".be/")[-1]
	else:
		video_id = video_url
	video_id = re.search("[\w-]+", video_id).group(0)

	yt = YouTube()
	yt.from_url("http://www.youtube.com/watch?v={}".format(video_id))
	yt.filter("mp4")[-1].download(path = folder_path, force_overwrite = True)


if __name__ == "__main__":
	for result in search("Megadeth - A Tout Le Monde"):
		print("{id}: ({duration}) {title}".format(**result))
	download("dQw4w9WgXcQ")
