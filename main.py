import keyboard
import os
import time
import pyautogui

amountRemove = 500

## Helpers ##
# esc close the loop

## Use python command line -> Save position to add in below code

#import pyautogui
#pyautogui.position()

def macro():
    for i in range(amountRemove):
        print('Remaining: '+str(500-i))
        pyautogui.click(-378, 161) # Change the position
        time.sleep(0.5)
        pyautogui.click(-320, 233) # Change the position
        time.sleep(0.5)
        pyautogui.click(-892, 572) # Change the position
        time.sleep(0.5)

def exit_on_key(keyname):
    def callback(event):
        if event.name == keyname:
            os._exit(1)
    return callback

if __name__ == '__main__':
    keyboard.hook(exit_on_key('esc'))
    macro()