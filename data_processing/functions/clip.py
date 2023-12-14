from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from os.path import join
from constants import CLIPS_PATH

def extract_clip(video_path: str, start: int, end: int, type: str, classification: int):
    output_path = join(CLIPS_PATH, f'{type}/{classification}/{video_path[video_path.index("videos/") + 7 : -4]}_{start}_{end}.mp4')
    ffmpeg_extract_subclip(video_path, start, end, output_path)
