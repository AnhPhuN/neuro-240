import openai
from sklearn.metrics.pairwise import cosine_similarity
import string


def get_embedding(text, model="text-embedding-ada-002"):
   text = text.replace("\n", " ")
   return openai.Embedding.create(input = [text], model=model)['data'][0]['embedding']


def get_similarity(text1, text2, model="text-embedding-ada-002"):
    embedding1 = get_embedding(text1, model)
    embedding2 = get_embedding(text2, model)
    similarity = cosine_similarity([embedding1], [embedding2])[0][0]
    print(f"Semantic similarity between the two strings: {similarity}")
    return similarity

text1 = """@ Arc File Edit View Spaces Tabs Archive Extensions Window Help $ [filler-1hi2mlet © @) TH CD GD Q Se SB MonMar 13 1:48 PM

=

data.txt — midterm Duta
i EXPLORER spy _init_.py =Zdatatxt X = labels.txt m -- {} pyautogui.press('left', presses=3)
v OPEN EDITORS = data.txt UIED > data > output > ocr > {}
keylog.py 1 1 ¢{
watchdog. py | ae To add a delay interval in between each press, pass an int or float for the keyword
euLCReLC Tog y) 3024, argument.
ee _init_.py /Libr... 3
Xx = data-txt l,
= "texts": [
= labels.txt The hold() Context Manager
file_load.py "id"
3 ‘al screenshot3.png "cor . . .
@ screenshot2.png "C0 To make holding a key convenient, the function can be used as a context manager and
v MIDTERM mic passed a string from the such as , L , and this key will
> co .
5 Le “rov be held for the duration of the context block. See KEYBOARD_KEYS.
"wic
> node_modules "he
> Ul-Automation ,
> UIED with pyautogui.hold('shift'):
> yoha a pyautogui.press(['left', ‘left',
active.py "co
autowatchdog.py "Tov
= data.txt "co equivalent to this code:
file_load.py mics
"wic
= key_log.txt "he
keylog.py , pyautogui.keyDown('shift') # hold down the shift key
= labels.txt pyautogui.press('left') # press the left arrow key
iipactacericcilecn "Gd" pyautogui.press(‘left') # press the left arrow key
D pecteraiton "cor pyautogui.press('left') # press the left arrow key
; "co pyautogui.keyUp('shift') # release the shift key
a] screenshot.png "roy
a] screenshot1.png "co
(| screenshot2.png "row
SE screenshot3.png i The hotkey() Function «
watchdog.py
OUTPUT DEBUGCONSOLE TERMINAL SQLCONSOLE -:- Python +v (] f} -- ~ x . .
— To make pressing hotkeys or keyboard shortcuts convenient, the can be passed
BRO Aa ab, * 4of4 x . A . . . .
BRE ° ° Pv several key strings which will be pressed down in order, and then released in reverse order. This
code:
sdf
BRO
13:41 .
: ry pyautogui.hotkey(‘ctrl', ‘shift', ‘esc')
> 13:44
> 13:44
> 13:45
..jiS equivalent to this code:
> 13:45
. 13:47 pyautogui.keyDown('ctrl')
https: //pyautogui. readthedocs. io/en/latest/keyboard. html pyautogui.keyDown( 'shift')
> 13:48 * ' 1
> Ci https://pyautogui. readthedocs. io/en/latest/keyboard.html pyautogui.keyDown('esc')
> TIMELINE yautogui. keyUp(‘esc')

x 8 fix-deprecation* @ @0OA\1 OConnect €LiveShare c tabnine starter UTF-8 LF PlainText @ Q@pPrettier & O as rn 55
"""

text2 = "work on essay about an AI that keeps you on task by looking at your screen and classifying if the stuff on the screen is on task"

def clean_text(raw_text):
    """
    Cleans raw text by removing non-alphabetic characters and keeping commas, periods, question marks, and exclamation marks.
    """
    valid_chars = set(string.ascii_letters + " " + ",.?!'\n")
    clean_text = ""

    for char in raw_text:
        if char.isalpha() or char in valid_chars:
            clean_text += char

    return clean_text

print(clean_text(text1))

get_similarity(clean_text(text1), text2)