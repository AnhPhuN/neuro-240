# create a python script that takes a screenshot of my macbook, 
# does OCR to get the text, gets the current active window, or 
# if it is a browser get the current URL of the website I am on. 

import pyautogui
import pytesseract
import time
from AppKit import NSWorkspace

time.sleep(1)
# Take screenshot
# screenshot = pyautogui.screenshot()

# Save screenshot to file
screenshot_path = 'screenshot4.png'
# screenshot.save(screenshot_path)

# Perform OCR on screenshot
text = pytesseract.image_to_string(screenshot_path)

# Get current active window
active_window = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
print('Active Window:', active_window)
print(text)

