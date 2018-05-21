import requests
import json
import sys
import os

def main():

    command= "youtube-dl --extract-audio --audio-format mp3 "
    songs = open(sys.argv[1]).readlines()
    for url in songs:
        os.system(command+url)

if __name__ == "__main__":
    main()
