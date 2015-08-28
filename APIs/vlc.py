import re
from subprocess import call


def mp4tomp3(input_file):
	output_file = re.sub("mp4$", "mp3", input_file)
	command = ["vlc", "--quiet", "-I", "dummy", "{input}".format(input = input_file), "--sout=#transcode{{acodec=mp3,vcodec=dummy}}:standard{{access=file,mux=raw,dst={output}}} vlc://quit".format(output = output_file)]
	call(command)


if __name__ == "__main__":
	mp4tomp3("../projects/Music/Man of the Year.mp4")
