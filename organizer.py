#!/usr/bin/python

from os import listdir
from os.path import isfile, join
import os
import sys

#check arguments
if len(sys.argv)<2:
    print("Usage: " + sys.argv[0] + " (target path)")
    sys.exit(1)

path = sys.argv[1]
files = [f for f in listdir(path) if isfile(join(path, f))]
files.sort(key=str.lower)
files.sort(key=len)

print("After sorting I have this order:")
for f in files:
    print(f)
response = raw_input("Is this correct? [y/n]")

if response != "y":
    print("Cancelling")
    sys.exit(1)

#TODO: get season data from TVDB
season = 1
response=raw_input("Next season number? (c cancels) [%d]" % season).lower()
while(response != "c"):
    if(response != ""):
        season = int(response)

    dirName = "Season %02d" % season
    targetDir = join(path,dirName)

    try:
        os.mkdir(targetDir)
    except:
        print("Directory already exists, cancelling as cautonary measure")
        sys.exit(1)

    response = raw_input("How many episodes? [%d]" % len(files))
    if(response == ""):
        numEpisodes = len(files)
    else:
        numEpisodes = int(response)

    response=raw_input("Will be moving %d episodes from %s to %s, press c to cancel" % (numEpisodes,path,targetDir)) 
    if response.lower == 'c':
        print("Cancelling")
        sys.exit(1)
    
    for i in range(numEpisodes):
        oldName = files[i]
        extension = oldName.split('.')[-1]
        if numEpisodes<100:
            newName = "S%02dE%02d.%s" % (season, i+1, extension)
        else:
            newName = "S%02dE%03d.%s" % (season, i+1, extension)

        oldFile = join(path,oldName)
        newFile = join(targetDir,newName)
        print("Moving from %s to %s" % (oldFile, newFile))
        os.rename(oldFile, newFile)

    #now remove them from the list
    files = files[numEpisodes:]

    if(len(files) == 0):
        print("No more files, DONE")
        sys.exit(0)

    season += 1
    response=raw_input("Next season number? (c cancels) [%d]" % season).lower()

print("Done")
