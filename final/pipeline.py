from getLabels import callAPI
from cleandataAPI import format_result
from collectPredictions import start_prompt
import pyautogui
import time
import json
import streamlit as st
import openai
import sys


def getCompletion(screen_content, user_prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.ChatCompletion.create(
    #   model="gpt-3.5-turbo",
      model="gpt-4",
      messages=[
            {"role": "system", "content": start_prompt},
            {"role": "user", "content": screen_content + "\n\n" + user_prompt}
        ]
    )
    return response['choices'][0]['message']['content']

start_prompt = """
You are taskGPT, an AI that takes in data taken from a computer screen and determines if someone is actually focused on a predefined task they gave. The format you take in is:
[x1,y1,x2,y2] “content info”
Where x1,y1,x2,y2 are integers that represent the bounding box pixel position of the text on the screen, counting from the top left with dimensions 3024 x 1964, and “content info” is the text contained inside the box.
Below is the content on the screen:
"""
suffix = """Am I on task? If I am, TaskGPT answers only 'Yes'. If not, TaskGPT says 'You are not on task', and gives an encouraging message to get back on task. TaskGPT is only allowed to choose yes or no."""

imgPath = "pipeline/screenshot.png"

# cont = input("press enter to continue")
# Create placeholders for emoji and completion message text boxes
process_text_box = st.empty()
user_prompt = st.text_input("Enter your current goal:")
emoji_text_box = st.empty()
completion_text_box = st.markdown("")
formatted_text_box = st.markdown("")

import os

def send_notification(title, subtitle, message):
    command = 'terminal-notifier -title "{}" -subtitle "{}" -message "{}"'.format(title, subtitle, message)
    os.system(command)

def save_screenshot(path):
    screenshot = pyautogui.screenshot()
    screenshot.save(path)

while True:
    while len(user_prompt) == 0:
        process_text_box.text("Waiting for user to input goal")
        time.sleep(.5)
    process_text_box.text("User inputted! " + user_prompt)
    time.sleep(2)
    process_text_box.text("screenshotting...")
    save_screenshot(imgPath)

    process_text_box.text("calling API...")
    json_obj = json.loads(callAPI(imgPath))
    
    process_text_box.text("OpenAI Completion on task: " + user_prompt)
    formatted_result = format_result(json_obj)
 
    print(formatted_result)
    formatted_text_box.text(formatted_result)
    completion = getCompletion(str(formatted_result), user_prompt + suffix)

    if completion == "Yes" or completion == "Yes.":
        emoji_text_box.text("😀")  # Smiley face
        completion_text_box.text("")
        send_notification("You're on task", "Subtitle", "Good job staying on task!")

  # Clear completion message text box
    else:
        emoji_text_box.text("☹️")  # Sad face
        completion_text_box.text(completion)
        send_notification("You're not on task", "Subtitle", completion)

