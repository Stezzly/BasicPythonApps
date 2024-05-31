import pyautogui
import time

def type_and_press_enter():
    while True:
        # Gives user 5 second to position the mouse to the chatGPT message bar and then click right click to select
        time.sleep(5)
        pyautogui.typewrite('continue')
        pyautogui.press('enter')
        time.sleep(60) # Waits for 60 seconds

if __name__ == "__main__":
    type_and_press_enter()

    