import re
from subprocess import call


def mp4tomp3(input_filepath, output_filepath = None):
	if output_filepath == None:
		output_filepath = re.sub("mp4$", "mp3", input_filepath)
	command = ["vlc", "--quiet", "-I", "dummy", "{input}".format(input = input_filepath), "--sout=#transcode{{acodec=mp3,vcodec=dummy}}:standard{{access=file,mux=raw,dst={output}}} vlc://quit".format(output = output_filepath)]
	call(command)


if __name__ == "__main__":
	infile = "../projects/Music/Man of the Year.mp4"
	mp4tomp3(infile)
	print("Converted file located at {}".format(re.sub("mp4$", "mp3", infile)))
