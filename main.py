from optparse import OptionParser
import os

from download import download
from search import search


if __name__ == "__main__":
	parser = OptionParser(description = "A tool for downloading YouTube videos. You can supply video IDs/URLs as any number of direct arguments, or put each on its own line in a list file and use the -f option. Use the -o option to specify the output directory. If you want to input video titles to search instead of a direct ID/URL (either as arguments or in a list =file), use the -s option.")
	parser.add_option("-f", "--fromfile", action = "store", dest = "fromfile", help = "specify a source file that contains newline-separated video IDs/URLs or search terms")
	parser.add_option("-o", "--outputdir", action = "store", dest = "outputdir", help = "specify the path to the directory where the videos will be saved")
	parser.add_option("-s", "--search", action = "store_true", dest = "search", default = False, help = "specify that the inputs are search queries rather than video IDs/URLs")
	options, args = parser.parse_args()
	if len(args) == 0 and not options.fromfile:
		print("use the -h flag for help!")


	path = options.outputdir+"/" if options.outputdir else "./"
	if not os.path.isdir(path):
		os.makedirs(path)

	for video in args:
		video_id = next(search(video))["id"] if options.search else video
		download(video_id, path)

	if options.fromfile:
		with open(options.fromfile, "r") as listfile:
			videos = listfile.read().split("\n")
		for video in videos:
			if video.strip():
				video_id = next(search(video))["id"] if options.search else video
				download(video_id, path)
