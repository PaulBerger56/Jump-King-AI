import pyautogui, time, pydirectinput, king_controller as kc, threading

# Initialized PyAutoGui
pyautogui.FAILSAFE = False
    
# Countdown timer
print("Starting", end="")
for i in range(0, 5):
    print(".", end="")
    time.sleep(1)
print("\nGo")

# t1 = threading.Thread(target=kc.pressJump(1.2))
# t2 = threading.Thread(target=kc.press_right(1.2))

# t1.start()
# t2.start()

# t1.join()
# t2.join()


# kc.pressJump(1.2)
# kc.press_right(1.2)
# pydirectinput.keyDown(key='space')
# pydirectinput.keyDown(key='_right')
# time.sleep(1.2)
# pydirectinput.keyUp(key='_right')  
# pydirectinput.keyUp(key='space')
kc.jump_right(1.2)

kc.jump_left(1.0)

kc.press_left(.1)  
  
kc.jump_right(1.2)

kc.jump_right(1.2)

kc.jump_left(1.2)

kc.press_right(.2)

kc.jump_left(1.2)

kc.jump_right(1.2)

kc.quick_jump_right()


# pydirectinput.keyDown(key='_right')
# time.sleep(.2)
# pydirectinput.keyDown(key='space')
# time.sleep(.1)
# pydirectinput.keyUp(key='space')
# time.sleep(.2)
# pydirectinput.keyUp(key='_right')

pydirectinput.keyDown(key='space')
pydirectinput.keyDown(key='right')
time.sleep(.3)
pydirectinput.keyUp(key='space')
pydirectinput.keyUp(key='right')

time.sleep(1)

pydirectinput.keyDown(key='space')
pydirectinput.keyDown(key='left')
time.sleep(.3) 
pydirectinput.keyUp(key='space')
pydirectinput.keyUp(key='left')

time.sleep(1)

pydirectinput.keyDown(key='left') 
pydirectinput.keyUp(key='left')

pydirectinput.keyDown(key='space') 
pydirectinput.keyDown(key='right')
time.sleep(.02)
pydirectinput.keyUp(key='space')
pydirectinput.keyUp(key='right')

pydirectinput.keyDown(key='space')
pydirectinput.keyDown(key='left')
time.sleep(.45) 
pydirectinput.keyUp(key='space')
pydirectinput.keyUp(key='left')

pydirectinput.keyDown(key='space')
pydirectinput.keyDown(key='left')
time.sleep(.7) 
pydirectinput.keyUp(key='space')
pydirectinput.keyUp(key='left')

pydirectinput.keyDown(key='space') 
pydirectinput.keyDown(key='right')
time.sleep(1.2)
pydirectinput.keyUp(key='space')
pydirectinput.keyUp(key='right')