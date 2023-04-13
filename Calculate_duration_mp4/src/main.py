from pathlib import Path
import moviepy
from moviepy.video.io.VideoFileClip import VideoFileClip


print (moviepy.__version__)
mp4_file = Path("/mnt/windows/Tutorials/Course/UDEMY/Python Django Dev To Deployment")

# variable for total time in seconds, minutes, and hours
total_time_second = 0
total_time_minute = 0
total_time_hour = 0

for count, filename in enumerate(Path(mp4_file).glob('*.mp4'), 1):
    clip = VideoFileClip(filename.as_posix())
    total_time_second += clip.duration
    # print (clip.duration, count)

total_time_minute = total_time_second / 60
total_time_hour = total_time_minute / 60

print (f"total time in second: {total_time_second}")
print (f"total time in minute: {total_time_minute}")
print (f"total time in hour: {total_time_hour}")
    


# mp4_file = list(desktop.glob("*.mp4"))
# # print (mp4_file)
# print (type(mp4_file))
# for file in  mp4_file:
#     print(str(file).split("/")[-1])