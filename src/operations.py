import ffmpeg
from pytube import YouTube
import json
import music_tag

class Operations:
    config_file_path = "src\config.json"
    #m4a is ideal
    file_types = [
         "m4a",
         "mp3",
         "aac",
         "aiff"
    ]
    with open(config_file_path, "r") as file:
            configuration = json.load(file)

    def __init__(self):
        pass

    def add_from_yt_link(file_link: str):
        pass

    def add_to_apple_music(file_path: str, type: str, properties: dict, song_name: str, artwork_path: str):
        file = music_tag.load_file(file_path)

       
        with open(artwork_path, 'rb') as img_in:
            file.append_tag('artwork', img_in.read())

        for tag in properties:
            try:
                property = properties[tag].get()
                if property != "": file[tag] = property
            except:
                return "Invalid Paramater Entered"
        
        file.save()

        folder = Operations.configuration["add_to_apple_music_path"]
        file_name = file_path[::-1]
        file_name = file_name[file_name.find('.')+1:file_name.find('/')]
        file_name = file_name[::-1]
        (
            ffmpeg
            .input(file_path)
            .output(folder + "/" + song_name + "." + type)
            .run()
        )
        return ""


if __name__ == "__main__":
    Operations()