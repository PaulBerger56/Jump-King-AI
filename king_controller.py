import pyautogui, time, pydirectinput

def press_left(press_time):
    pydirectinput.keyDown(key='left')
    time.sleep(press_time) 
    pydirectinput.keyUp(key='left')

def press_right(press_time):
    pydirectinput.keyDown(key='right')
    time.sleep(press_time) 
    pydirectinput.keyUp(key='right')

def press_jump(press_time):
    pydirectinput.keyDown(key='space')
    time.sleep(press_time) 
    pydirectinput.keyUp(key='space')

def jump_left(press_time):
    pydirectinput.keyDown(key='space')
    pydirectinput.keyDown(key='left')
    time.sleep(press_time) 
    pydirectinput.keyUp(key='left')
    pydirectinput.keyUp(key='space')

def jump_right(press_time):
    pydirectinput.keyDown(key='space')
    pydirectinput.keyDown(key='right')
    time.sleep(press_time) 
    pydirectinput.keyUp(key='right')
    pydirectinput.keyUp(key='space')
    
def quick_jump_right():
    pydirectinput.keyDown(key='right')
    time.sleep(.2)
    pydirectinput.keyDown(key='space')
    time.sleep(.1)
    pydirectinput.keyUp(key='space')
    time.sleep(.2)
    pydirectinput.keyUp(key='right')
    
def quick_jump_left():
    pydirectinput.keyDown(key='left')
    time.sleep(.2)
    pydirectinput.keyDown(key='space')
    time.sleep(.1)
    pydirectinput.keyUp(key='space')
    time.sleep(.2)
    pydirectinput.keyUp(key='left')

