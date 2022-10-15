import pytube, json
import whisper


print('Youtube Downloader'.center(40, '_'))
# URL = input('Enter youtube url :  ')
URL = "https://www.youtube.com/watch?v=HSVjz4FPKzM"
video = URL #"https://www.youtube.com/watch?v=HSVjz4FPKzM" #"https://www.youtube.com/watch?v=ad79nYk2keg&t=3s"
data = pytube.YouTube(video)
# print(data.title)

# Converting and downloading as 'MP4' file
audio = data.streams.get_audio_only()
src = audio.download()
# print(src)

# result of success
print(data.title + " has been successfully downloaded.")

model = whisper.load_model("small") # large for accuracy
result = model.transcribe(src)

# Serializing json
json_object = json.dumps(result, indent=4)

# Writing to sample.json
with open(data.title + ".json", "w") as outfile:
    outfile.write(json_object)


"""# YouTube Transcribe API"""

# !pip install youtube_transcript_api

# from youtube_transcript_api import YouTubeTranscriptApi
# import os

# srt = YouTubeTranscriptApi.get_transcript("NU5sn_Pn6pU")
# print(srt)

