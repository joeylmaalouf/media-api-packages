from pytube import YouTube
import re


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
	download("dQw4w9WgXcQ")
