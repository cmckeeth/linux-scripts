from os import listdir
from os.path import isfile, join
from os import walk


mypath = "~/PlexLibrary/Movies/buffer";

f = []

for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break


for file in f:
	print("file: " + file + "\n")


