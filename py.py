import pyautogui,os,time

scrnW, scrnH = pyautogui.size() # Get the size of the primary monitor.

# while 1:
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
print(currentMouseX,currentMouseY)
time.sleep(0.05)
    # os.system("cls")

# pyautogui.moveTo(scrnW, 0) # Move the mouse to XY coordinates.

# pyautogui.click()          # Click the mouse.
pyautogui.click(scrnW-20, 20, button='left')  # Move the mouse to XY coordinates and click it.
pyautogui.click(scrnW//2, int(scrnH*0.53), button='left')
# pyautogui.click('button.png') # Find where button.png appears on the screen and click it.

# pyautogui.move(400, 0)      # Move the mouse 400 pixels to the right of its current position.
# pyautogui.doubleClick()     # Double click the mouse.
# pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.

# pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
# pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES

# with pyautogui.hold('shift'):  # Press the Shift key down and hold it.
#         pyautogui.press(['left', 'left', 'left', 'left'])  # Press the left arrow key 4 times.
# # Shift key is released automatically.

# pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.

# pyautogui.alert('This is the message to display.') # Make an alert box appear and pause the program until OK is clicked.