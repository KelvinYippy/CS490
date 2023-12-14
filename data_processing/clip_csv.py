import csv
from constants import VIDEOS_PATH, MAIN_PATH
from utils import get_youtube_video_id, convert_to_seconds, add_to_file
from functions.download import download_video_no_audio, download_video_with_audio
from functions.clip import extract_clip
from os.path import isfile, join
from pytube.exceptions import AgeRestrictedError, VideoPrivate
from datetime import datetime

def download_and_clip_from_csv(csv_path: str, with_sound: bool):
    timestamp = datetime.now()
    phrase = csv_path[csv_path.rindex("/") + 1 : csv_path.rindex(".")]
    error_log_file = join(MAIN_PATH, "files", "logs", f"{phrase}_{timestamp}.txt")
    type = phrase[:-1]
    classification = phrase[-1]
    with open(csv_path, newline='') as csvfile:
        clips = csv.reader(csvfile, delimiter=',', quotechar='|')
        for clip in clips:
            link, start, end = clip
            file_path = f"{VIDEOS_PATH}/{get_youtube_video_id(link)}.mp4"
            try:
                if not isfile(file_path):
                    if with_sound:
                        download_video_with_audio(link)
                    else:
                        download_video_no_audio(link)
                extract_clip(file_path, convert_to_seconds(start), convert_to_seconds(end), type, classification)
            except AgeRestrictedError:
                add_to_file(error_log_file, f"{link} | Reason: Age Restricted")
            except VideoPrivate:
                add_to_file(error_log_file, f"{link} |  Reason: Video Private")
            
download_and_clip_from_csv("./education0.csv", False)
download_and_clip_from_csv("./education1.csv", False)
download_and_clip_from_csv("./sports0.csv", False)
download_and_clip_from_csv("./sports1.csv", False)
download_and_clip_from_csv("./politics0.csv", False)
download_and_clip_from_csv("./politics1.csv", False)