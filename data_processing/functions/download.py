from pytube import YouTube
import os
import moviepy.editor as mpe
from constants import VIDEOS_PATH

def download_video_with_audio(url: str):
    youtube = YouTube(url)
    audio = youtube.streams.get_audio_only().download()
    os.rename(audio, "audio.mp3")
    video = youtube.streams.filter(file_extension="mp4").order_by("resolution").last().download()
    os.rename(video, "video.mp4")
    transitioned_video = mpe.VideoFileClip("video.mp4")
    transitioned_audio = mpe.AudioFileClip("audio.mp3")
    final_video: mpe.VideoClip = transitioned_video.set_audio(transitioned_audio)
    final_video.write_videofile(os.path.join(VIDEOS_PATH, f'{url[url.index("?v=") + 3:]}.mp4'))
    os.remove("audio.mp3")
    os.remove("video.mp4")

def download_video_no_audio(url: str):
    youtube = YouTube(url)
    youtube = youtube.streams.filter(file_extension="mp4").order_by("resolution").last()
    youtube.download(VIDEOS_PATH, filename=f'{url[url.index("?v=") + 3:]}.mp4')
