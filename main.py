#!/usr/bin/env python

from pytube import YouTube
from pydub import AudioSegment
from pprint import pprint
import time
import os, sys
import glob

"""
    Set output folder name and source list for download from youtube
"""
output_folder = "videos"
audio_folder = "audio"
video_urls = [
"https://www.youtube.com/watch?v=taENjQXJbl8",
# "https://www.youtube.com/watch?v=ZvA0uO66qoc"
]

EXTRACT_AUDIO = True
extension_list = ('*.mp4', '*.flv')

STAMP = str(time.time()).split(".")[0]
BASE = os.path.dirname(os.path.abspath(__file__))
output_path =  os.path.join(BASE, output_folder)
output_audio_path =  os.path.join(output_path, audio_folder)

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


    # extarct audios
    if EXTRACT_AUDIO:
        if not os.path.exists(output_audio_path):
            os.makedirs(output_audio_path)

        os.chdir(output_path)
        for extension in extension_list:
            for video in glob.glob(extension):
                mp3_filename = os.path.splitext(os.path.basename(video))[0] + '.mp3'
                mp3_path =  os.path.join(output_audio_path, mp3_filename)
                AudioSegment.from_file(video).export(mp3_path, format='mp3')

