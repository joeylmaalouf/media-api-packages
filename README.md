# YouTube Downloader

This program allows the user to download any number of YouTube videos, using either IDs/URLs or search terms.


## Options:

`-f FROMFILE, --fromfile=FROMFILE`: specify a source file that contains newline-separated video IDs/URLs or search terms

`-o OUTPUTDIR, --outputdir=OUTPUTDIR`: specify the path to the directory where the videos will be saved

`-s, --search`: specify that the inputs are search queries rather than video IDs/URLs


## Example Usage:

`python main.py youtu.be/dQw4w9WgXcQ`

`python main.py \"doot doot\" --search`

`python main.py --fromfile rhcp.txt --outputdir Music/RHCP`

`python main.py -s -f hu.txt -o Music/HU`


## Thanks To:

[PyTube!](https://github.com/nficano/pytube)
