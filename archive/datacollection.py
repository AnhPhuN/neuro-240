import time
import pyautogui
from PIL import Image
import pytesseract
import pyperclip





# Wait for 5 seconds before starting
time.sleep(1)

# Press Cmd + l to highlight the address bar
with pyautogui.hold('command'):
    pyautogui.press('l')

# Wait for 1 second before copying the address
time.sleep(1)

# Press Cmd + c to copy the address
pyautogui.hotkey('command', 'c')
url = pyperclip.paste()
print(url)


# Press Esc to clear the address bar
pyautogui.press('esc')

# Wait for 1 second before taking a screenshot
time.sleep(1)

# Take a screenshot of the entire screen
screenshot = pyautogui.screenshot()

# Save the screenshot to a file
screenshot.save('screenshot.png')

# Use Pytesseract to OCR the screenshot and extract text
text = pytesseract.image_to_string(Image.open('screenshot.png'))

# Write the text and labels to files
with open('data.txt', 'a') as data_file, open('labels.txt', 'a') as labels_file:
    data_file.write(text + "\n###") # delimiter
    labels_file.write(url + "\n###") # delimiter
