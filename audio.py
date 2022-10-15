import whisper
import json 

# importing packages
from pytube import YouTube
import os
  
# "https://www.youtube.com/watch?v=HSVjz4FPKzM", "https://www.youtube.com/watch?v=2ePf9rue1Ao"

# url input from user
yt = YouTube(
    str(input("Enter the URL of the video you want to download: \n>> ")))

# extract only audio
video = yt.streams.filter(only_audio=True).first()
  
# check for destination to save file
destination = '.'
  
# download the file
out_file = video.download(output_path=destination)
  
# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.wav'
os.rename(out_file, new_file)
  
# result of success
print(yt.title + " has been successfully downloaded.")

model = whisper.load_model("base")
result = model.transcribe(new_file)

# Serializing json
json_object = json.dumps(result, indent=4)
 
# Writing to sample.json
with open(base + ".json", "w") as outfile:
    outfile.write(json_object)

print(result['text'])