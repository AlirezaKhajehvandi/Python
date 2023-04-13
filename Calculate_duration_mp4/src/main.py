from pathlib import Path
from moviepy.video.io.VideoFileClip import VideoFileClip

desktop = Path("/mnt/windows/Tutorials/Course/UDEMY/Python Django Dev To Deployment")
print ("alireza khajehvnadi")
print (Path.cwd())

for filename in Path(path2).glob('*.mp4'):
    clip = VideoFileClip(filename.as_posix())
    print(clip.duration)


mp4_file = list(desktop.glob("*.mp4"))
# print (mp4_file)
print (type(mp4_file))
for file in  mp4_file:
    print(str(file).split("/")[-1])