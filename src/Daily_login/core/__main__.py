import numpy as np
import cv2
import pyautogui
import time
import os
import utils.image_recognition as img_recognition
import utils.find_window as fw


img_playButton = "/assets/img/play_button.png"
launcher_window = "RotMG Exalt Launcher"
game_window = "RotMGExalt"

def main():
	opengame = "steam://rungameid/200210"
	if os.name == 'nt':  # Windows
		os.system(f'start {opengame}')
	else:  # Linux/Mac
		os.system(f'xdg-open {opengame}')

	fw.find_window(launcher_window)

	# Check if the play button is visible
	if img_recognition.wait_for_image("img_playButton", timeout=30, confidence=0.9):
		img_recognition.click_image("img_playButton", confidence=0.9)
	else:
		print("Play button not found, exiting.")
		return

	# Wait for the game to load after clicking play
	time.sleep(5)	
img_recognition.wait_for_image("img_playButton", timeout=30, confidence=0.9)
img_recognition.click_image("img_playButton", confidence=0.9)

