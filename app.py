import streamlit as st
import whisper
import json 
from pytube import YouTube
import os

st.set_page_config(layout="wide", page_title="YouTube Transcription", page_icon=":book:")

status = "pending"
title = ""

if 'status' not in st.session_state:
    st.session_state['status'] = 'submitted'
 
@st.cache
def transcribe_from_link(link):
	print("Transcribing...")	
	# "https://www.youtube.com/watch?v=HSVjz4FPKzM"

	# url input from user
	yt = YouTube(link)
	global title
	title = yt.title

	# check if file exists
	if not os.path.exists("transcript/" + yt.title + ".json"):
		# extract only audio
		video = yt.streams.filter(only_audio=True).first()
		
		# check for destination to save file
		destination = '.'
		
		# download the file
		out_file = video.download(output_path=destination)
		
		# save the file
		base, ext = os.path.splitext(out_file)
		new_file = base + '.mp3'
		os.rename(out_file, new_file)
		
		# result of success
		print(yt.title + " has been successfully downloaded.")

		model = whisper.load_model("base")
		result = model.transcribe(new_file)

		# Serializing json
		json_object = json.dumps(result, indent=4)
		
		# Writing to sample.json
		with open("transcript/" + base + ".json", "w") as outfile:
			outfile.write(json_object)

		print(result['text'])
		
		# delete the mp3 file
		if os.path.exists(new_file):
			os.remove(new_file)
			print("The file has been deleted successfully")
		else:
			print("The file does not exist!")

	# Change status to completed	
	global status 
	status = "completed"

	return "completed"


def get_status():
	st.session_state['status'] = status

def refresh_state():
	global status
	status = 'submitted'
	st.session_state['status'] = 'submitted'

st.title('Easily transcribe YouTube videos')

col1, col2 = st.columns(2)

with col1:
	link = st.text_input('Enter your YouTube video link', '', on_change=refresh_state)
	if link != "":
		st.video(link)

with col2:
	st.text("The transcription is " + st.session_state['status'])

	if link != "":
		polling_endpoint = transcribe_from_link(link)
		st.button('check_status', on_click=get_status)

	transcript=''
	if st.session_state['status']=='completed':
		yt = YouTube(link)
		YT_title = yt.title
		f = open("transcript/" + YT_title + '.json')
		data = json.load(f)
		transcript = data['text']
		f.close()

	st.markdown(transcript)




 