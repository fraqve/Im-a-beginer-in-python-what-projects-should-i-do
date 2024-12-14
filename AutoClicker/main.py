import time
from pynput.mouse import Controller , Button
from pynput.mouse import *
from pynput.keyboard import Listener , KeyCode
import threading
toggle_key = KeyCode(char="r")
toggle_keyr = KeyCode(char="v")
mouse = Controller()
is_clicking = False
is_clickingr = False
interval = 0.05
def autoclick():
    global is_clicking
    while True:
        if is_clicking == True:
            mouse.click(Button.left , 1)
        time.sleep(interval)

def autoclickr():
    global is_clickingr
    while True:
        if is_clickingr == True:
            mouse.click(Button.right , 1)
        time.sleep(interval)


def toggle(key):
    global is_clicking
    if key == toggle_key:
        is_clicking = not is_clicking
    global is_clickingr
    if key == toggle_keyr:
        is_clickingr = not is_clickingr




mouse_th = threading.Thread(target=autoclick)
mouse_th.start()

mouse_thR = threading.Thread(target=autoclickr)
mouse_thR.start()



with Listener(on_press=toggle) as l:
    l.join()



