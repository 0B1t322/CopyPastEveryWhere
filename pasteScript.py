import clipboard
import pyautogui
import keyboard
import time

def paste():
    text = clipboard.paste()
    time.sleep(1)
    pyautogui.write(text,interval=0.01)


keyboard.add_hotkey("Ctrl + Shift + H", paste )

keyboard.wait("Ctrl + Q")

