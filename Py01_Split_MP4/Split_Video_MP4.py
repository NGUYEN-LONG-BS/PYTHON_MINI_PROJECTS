# Note
# Cut .mp4 in pieces Python
# Source: https://stackoverflow.com/questions/67334379/cut-mp4-in-pieces-python
# How to get the duration of a video in Python?
# Source: https://stackoverflow.com/questions/3844430/how-to-get-the-duration-of-a-video-in-python
# Creating thumbnails from video files with Python
# Source: https://stackoverflow.com/questions/1772599/creating-thumbnails-from-video-files-with-python
# install library moviepy: pip3 install moviepy

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Replace the filename below.
required_video_file = "01 - QUANT - Buổi 1 - 18.08.mp4"

with open("times.txt") as f:
  times = f.readlines()

times = [x.strip() for x in times]

for time in times:
  starttime = int(time.split("-")[0])
  endtime = int(time.split("-")[1])
  ffmpeg_extract_subclip(required_video_file, starttime, endtime, targetname=str(times.index(time)+1)+".mp4")

# Đo thời lượng của video
# filename = required_video_file
# def with_moviepy(filename):
#     from moviepy.editor import VideoFileClip
#     clip = VideoFileClip(filename)
#     duration       = clip.duration
#     fps            = clip.fps
#     width, height  = clip.size
#     return duration, fps, (width, height)
  
