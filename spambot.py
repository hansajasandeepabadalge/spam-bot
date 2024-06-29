import pyautogui
import time

message = "This is a spam msg"
n = 20

pyautogui.PAUSE = 1

print("You have 5 seconds to switch to the WhatsApp Web chat window.")
time.sleep(5)

for i in range(n):
    pyautogui.typewrite(message)
    pyautogui.press('enter')
    time.sleep(0.2)

print(f"Sent the message {n} times.")
