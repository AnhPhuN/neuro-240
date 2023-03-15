import time
import pyautogui
from PIL import Image
import pytesseract
import pyperclip

with pyautogui.hold('command'):
    pyautogui.press('l')

time.sleep(3)
with open("data/urls.txt", "r") as file:
    for i, url in enumerate(file):
        print("Doing Line {}: {}".format(i, url))
        # Press Cmd + l to highlight the address bar
        with pyautogui.hold('command'):
            time.sleep(.1)
            pyautogui.press('l')
        time.sleep(.1)
        # type the address of "line"
        pyautogui.typewrite(url)
        pyautogui.press('enter')
        time.sleep(3)

        # Take a screenshot of the entire screen
        screenshot = pyautogui.screenshot()
        screenshot.save("data/screenshots/" + str(i) + '.png')
        text = pytesseract.image_to_string(Image.open('data/screenshots/' + str(i)+ '.png'))

        # Write the text to files
        with open('data/text/' + str(i) + '.txt', 'a') as data_file:
            data_file.write(text + "\n###") # delimiter





