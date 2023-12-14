from os.path import getsize

def get_youtube_video_id(link: str):
    return link[link.index("v=") + 2:]

def convert_to_seconds(timestamp: str):
    seconds = 0
    times = timestamp.split(":")
    for t in times:
        seconds *= 60 
        seconds += int(t)
    return seconds

def add_to_file(path: str, new_content: str):
    """
        Add text to the file provided by the path
        path : str
            The path of where the file is located
        new_content : str
            The new text content to append to the file
    """
    with open(path, "a") as f:
        if getsize(path) > 0:
            f.write("\n")
        f.write(new_content)
    f.close()