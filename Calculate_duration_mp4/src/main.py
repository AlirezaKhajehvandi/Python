# importing necessary modules
from pathlib import Path
from tqdm.auto import tqdm
from moviepy.video.io.VideoFileClip import VideoFileClip

# Choose yout path (put your path instead of 'your path')
mp4_file = Path("your path")

# variable for total time in seconds, minutes, and hours
total_time_second = 0
total_time_minute = 0
total_time_hour = 0

# looping to get the duration of any file
for count, filename in tqdm(enumerate(Path(mp4_file).glob('*.mp4'), 1)):
    clip = VideoFileClip(filename.as_posix())
    total_time_second += clip.duration
    # print (clip.duration, count)

# calculating duration for mp4 files in the specific path
total_time_minute = total_time_second / 60
total_time_hour = total_time_minute / 60

# showing results
print (f"total time in second: {total_time_second} seconds")
print (f"total time in minute: {total_time_minute} minutes")
print (f"total time in hour: {total_time_hour} hours")
print (f"number of files: {count}")
    