from pytube import Playlist, YouTube
import re

#python3 -m pip install --upgrade "git+https://github.com/nficano/pytube.git"

playlist = Playlist("https://youtube.com/playlist?list=PLrqeR7Lk2888cZ7RIx6jj_ZDyJWAddmg-")
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

for url in playlist.video_urls:
    print(url)
    try:
        yt_obj = YouTube(url)
        yt_obj.streams.filter(only_audio=True).first().download() #For Mp3 Only
       # yt_obj.streams.get_highest_resolution().download() #For Mp4 Only
    except Exception as e:
        print(e)
        raise Exception('Some exception occurred.')
  
    print('YouTube Videos Downloaded Successfully....')
  