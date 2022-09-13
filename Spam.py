import pyautogui
import time

time.sleep(5)
i = 0

while i < 5:
    pyautogui.write("Python test")
    pyautogui.press("enter")
    i += 1

exit(0)
