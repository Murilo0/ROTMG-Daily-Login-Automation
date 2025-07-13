import subprocess
import sys
import time
import pyautogui

steam_command = "steam://run/200210"

print("Initializing the game...")

try:
    if sys.platform == "win32":  # Windows
        import os
        os.startfile(steam_command)
    elif sys.platform == "darwin":  # macOS
        subprocess.run(["open", steam_command], check=True)
    else:  # Linux
        subprocess.run(["xdg-open", steam_command], check=True)
    
    print("Command executed successfully.")

except Exception as e:
    print(f"Error initializing the game: {e}")
    print("Check if Steam is installed and the game is available in your library.")
    sys.exit()  # Exit the script if the game could not be launched

print("Waiting for the game to load...")

play_button = 'play_button.png'  # Image of the game's "Play" button
max_wait_time = 120  # Maximum wait time in seconds (2 minutes)
start_time = time.time()
game_window = None

while time.time() - start_time < max_wait_time:
    game_window = pyautogui.locateOnScreen(play_button, confidence=0.8)
    if game_window:
        print("Game detected on screen! Continuing with automation.")
        break
    else:
        print("Game not detected yet, waiting 5 seconds...")
        time.sleep(5)
else:
    print("Wait time exceeded. The game was not detected on the screen.")
    sys.exit()
print("Wait time finished. Attempting to automate login...")

