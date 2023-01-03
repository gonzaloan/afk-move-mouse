import pyautogui as pyautogui
import random
import time

while True:
	x = random.randint(600,700)
	y = random.randint(200,600)
	pyautogui.moveTo(x,y,0.3)
	pyautogui.FAILSAFE = False
	time.sleep(3)
