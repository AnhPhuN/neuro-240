# get active window screenshot only the

import pyautogui
import pygetwindow

# Get the active window
window = pygetwindow.getActiveWindow()
print(window)

# Get the position and size of the active window
x, y, width, height = window.topleft + window.size

# Take a screenshot of the active window
screenshot = pyautogui.screenshot(region=(x, y, width, height))

# Save the screenshot to a file
screenshot.save('screenshot.png')