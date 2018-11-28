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
output_folder = "downloads"
audio_folder = "audio"
video_urls = [
'https://www.youtube.com/watch?v=TQHs8SA1qpk'
]

EXTRACT_AUDIO = True
EXTRACT_SUBTITLE = True
extension_list = ('*.mp4', '*.flv')

BASE = os.path.dirname(os.path.abspath(__file__))
output_path =  os.path.join(BASE, output_folder)
output_audio_path =  os.path.join(output_path, audio_folder)

if __name__ == "__main__":

    if not os.path.exists(output_path):
        os.makedirs(output_path)


    for video_path in video_urls:
        print ("Get %s" % video_path)
        yt = YouTube(video_path)
        
        if EXTRACT_SUBTITLE:
            file_name = os.path.join(output_path, '{0}.txt'.format(yt.title))
            file = open(file_name,'w')
            file.write(yt.captions.get_by_language_code('en').generate_srt_captions())
            file.close()

        yt.streams.filter(progressive=True, file_extension='mp4')\
            .order_by('resolution')\
            .desc()\
            .first()\
            .download(output_path)

        print("Sleeping...")
        time.sleep(2)


    # extarct audios
    if EXTRACT_AUDIO:
        if not os.path.exists(output_audio_path):
            os.makedirs(output_audio_path)

        os.chdir(output_path)
        for extension in extension_list:
            print(extension)
            for video in glob.glob(extension):
                mp3_filename = os.path.splitext(os.path.basename(video))[0] + '.mp3'
                mp3_path =  os.path.join(output_audio_path, mp3_filename)
                AudioSegment.from_file(video).export(mp3_path, format='mp3')

