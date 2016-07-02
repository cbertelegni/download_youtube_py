from pytube import YouTube
from pprint import pprint
import time

video_urls = [
"https://www.youtube.com/watch?v=GRHxHapwirw",
"https://www.youtube.com/watch?v=kVX0GtLxRjE"
]

STAMP = str(time.time()).split(".")[0]
for video_path in video_urls:  
    yt = YouTube(video_path)
    pprint(yt.get_videos())
    # video = yt.get('mp4')
    """ get the better quality """
    video = yt.filter('mp4')[-1]
    if video:
        # view the auto generated filename:
        # print(yt.filename)
        # set the filename
        yt.set_filename("%s_%s" % (STAMP, yt.filename))
        video.download('./videos/')
    else:
        print("not mp4 video format for: %s \n" % (video_path))

    print("Sleeping 10 seconds")
    time.sleep(10)
