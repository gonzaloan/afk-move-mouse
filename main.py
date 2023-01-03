import pyautogui
import time

while True:
    pyautogui.moveRel(10, 0, duration=0.1)
    pyautogui.moveRel(0, 10, duration=0.1)
    pyautogui.moveRel(-10, 0, duration=0.1)
    pyautogui.moveRel(0, -10, duration=0.1)
    time.sleep(2)