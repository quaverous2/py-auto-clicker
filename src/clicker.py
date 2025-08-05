import pyautogui
import keyboard
import time
import threading

clicking = False

def click_loop():
    while True:
        if clicking:
            pyautogui.click()
            time.sleep(0.01)  # Adjust click speed
        else:
            time.sleep(0.01)

def toggle_clicking():
    global clicking
    clicking = not clicking
    print("Clicking ON" if clicking else "Clicking OFF")

def main():
    print("Press F9 to toggle auto clicker. Press ESC to quit.")
    thread = threading.Thread(target=click_loop)
    thread.daemon = True
    thread.start()

    keyboard.add_hotkey('F9', toggle_clicking)
    keyboard.wait('esc')

if __name__ == "__main__":
    main()
