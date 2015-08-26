import re
import requests


def search(query):
	response = requests.get("https://www.youtube.com/results?search_query={}".format(query))
	matches = re.findall("<h3.*<a href.+</a><span.+</span></h3>", response.content)
	for match in matches:
		if "Duration" in match: # make sure it's a video, not a playlist
			video_id = re.search("v=[-,_,a-z,A-Z,0-9,]+", match).group(0)[2:]
			video_title = re.search("ltr\">.+</a>", match).group(0)[5:-4]
			video_duration = re.search("Duration:.*[.]", match).group(0)[10:-1]
			yield {"id":video_id, "title":video_title, "duration":video_duration}


if __name__ == "__main__":
	for result in search("Megadeth - A Tout Le Monde"):
		print("{id}: ({duration}) {title}".format(**result))
