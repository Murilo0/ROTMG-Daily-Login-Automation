import pygetwindow as gw
import time
import pyautogui

def find_window(window_name: str):
    print("Waiting for the game window to appear...")
    game_window = None
    while game_window is None:
        try:
            game_window = gw.getWindowsWithTitle(window_name)[0]
        except IndexError:
            time.sleep(1)
    
    print(f"Window '{window_name}' found.")
    game_window.activate()