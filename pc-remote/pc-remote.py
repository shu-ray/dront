import keyboard
import time
import simplepyble

key_state = False
def is_bump(key):
    global key_state
    if key != key_state:
        if key_state == False:
            key_state = True
            return True
        if key_state == True:
            key_state = False
            return False
    return -1





while True:
    #print(is_bump(keyboard.is_pressed("ctrl+alt+z")))
    print(is_bump(keyboard.is_pressed("s")))
    time.sleep(0.1)