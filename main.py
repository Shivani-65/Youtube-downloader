
from pytube import YouTube
url="https://youtu.be/vf-XIsSWiGA"
my_video=YouTube(url)
s=my_video.streams.get_highest_resolution()
s.download()
