from getLabels import callAPI
from cleandataAPI import format_result
from collectPredictions import start_prompt, getCompletion
import pyautogui
import time
import json
import streamlit as st


suffix = """Am I on task? If 
I am, TaskGPT answers only 'Yes'. If not, TaskGPT says 'You are not on task', 
and gives an encouraging message to get back on task"""
imgPath = "screenshot.png"
user_prompt = """I am trying to check my email."""

# cont = input("press enter to continue")
# Create placeholders for emoji and completion message text boxes
process_text_box = st.empty()
emoji_text_box = st.empty()
completion_text_box = st.markdown("")


while True:
    time.sleep(1)
    process_text_box.text("screenshotting...")
    screenshot = pyautogui.screenshot()
    screenshot.save(imgPath)

    process_text_box.text("calling API...")
    json_string = callAPI(imgPath)
    json_obj = json.loads(json_string)
    
    process_text_box.text("OpenAI Completion...")
    formatted_result = format_result(json_obj)
    completion = getCompletion(str(formatted_result), user_prompt+suffix)

    if completion == "Yes" or completion == "Yes.":
        emoji_text_box.text("😀")  # Smiley face
        completion_text_box.text("")
  # Clear completion message text box
    else:
        emoji_text_box.text("☹️")  # Sad face
        completion_text_box.text(completion)

