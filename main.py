#!/usr/bin/env python

from pytube import YouTube
from pprint import pprint
import time
import os, sys

"""
    Set output folder name and source list for download from youtube
"""
output_folder = "videos"
video_urls = [
"https://www.youtube.com/watch?v=taENjQXJbl8",
"https://www.youtube.com/watch?v=ZvA0uO66qoc",
"https://www.youtube.com/watch?v=qM_5YzToXRw"
]



STAMP = str(time.time()).split(".")[0]
BASE = os.path.dirname(os.path.abspath(__file__))
output_path =  os.path.join(BASE, output_folder)

if __name__ == "__main__":

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for video_path in video_urls:  
        yt = YouTube(video_path)
        pprint(yt.get_videos())
        # video = yt.get('mp4')
        """ get the better quality """
        video = yt.filter('mp4')[0]
        # video = yt.filter('mp4')[-1] # the best quality
        if video:
            # view the auto generated filename:
            # print(yt.filename)
            # set the filename
            yt.set_filename("%s_%s" % (STAMP, yt.filename))
            video.download(output_path)
        else:
            print("not mp4 video format for: %s \n" % (video_path))

        print("Sleeping...")
        time.sleep(2)
