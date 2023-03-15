import time
from pynput import keyboard
import subprocess

start_time = int(time.time() * 1000)

with open("key_log.txt", "w") as f:
    f.write("")

def on_press(key):
    timestamp = int(time.time() * 1000)
    with open("key_log.txt", "a") as f:
        f.write(f"{timestamp - start_time}, {key}\n")


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()