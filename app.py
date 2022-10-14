import streamlit as st
# import os
# from dotenv import load_dotenv

# load_dotenv()
# value = os.getenv("API_KEY")
# print(value)

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="YouTube Transcription", page_icon=":book:")

if 'status' not in st.session_state:
    st.session_state['status'] = 'submitted'
 
@st.cache
def transcribe_from_link(link, categories: bool):
	print("Transcribing...")

	return "abc"


def get_status(polling_endpoint):
	# polling_response = requests.get(polling_endpoint, headers=headers)
	st.session_state['status'] = "completed"

def refresh_state():
	st.session_state['status'] = 'submitted'


st.title('Easily transcribe YouTube videos')

col1, col2 = st.columns(2)

with col1:
	link = st.text_input('Enter your YouTube video link', 'https://youtu.be/dccdadl90vs', on_change=refresh_state)
	st.video(link)

with col2:
	st.text("The transcription is " + st.session_state['status'])

	polling_endpoint = transcribe_from_link(link, False)

	st.button('check_status', on_click=get_status, args=(polling_endpoint,))

	transcript=''
	if st.session_state['status']=='completed':
		f = open("transcript.txt")
		transcript = f.read()
		f.close()

	st.markdown(transcript)




 