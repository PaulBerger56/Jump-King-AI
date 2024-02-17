import pyautogui, time, pydirectinput

# Initialized PyAutoGui
pyautogui.FAILSAFE = False
    
# Countdown timer
print("Starting", end="")
for i in range(0, 5):
    print(".", end="")
    time.sleep(1)
print("\nGo")

pydirectinput.keyDown(key='space')
pydirectinput.keyDown(key='right')
time.sleep(1.2)
pydirectinput.keyUp(key='right') 
pydirectinput.keyUp(key='space')

pydirectinput.keyDown(key='space')
pydirectinput.keyDown(key='left')
time.sleep(1.0) 
pydirectinput.keyUp(key='left')
pydirectinput.keyUp(key='space')


pydirectinput.keyDown(key='left')
time.sleep(.2) 
pydirectinput.keyUp(key='left')

pydirectinput.keyDown(key='space')
pydirectinput.keyDown(key='right')
time.sleep(1.2)
pydirectinput.keyUp(key='space')
pydirectinput.keyUp(key='right')

pydirectinput.keyDown(key='space')
pydirectinput.keyDown(key='right')
time.sleep(1.2)
pydirectinput.keyUp(key='space')
pydirectinput.keyUp(key='right')

pydirectinput.keyDown(key='space')
pydirectinput.keyDown(key='left')
time.sleep(1.2) 
pydirectinput.keyUp(key='space')
pydirectinput.keyUp(key='left')

pydirectinput.keyDown(key='right')
time.sleep(.2) 
pydirectinput.keyUp(key='right')

pydirectinput.keyDown(key='space')
pydirectinput.keyDown(key='left')
time.sleep(1.2) 
pydirectinput.keyUp(key='space')
pydirectinput.keyUp(key='left')
    
pydirectinput.keyDown(key='space')
pydirectinput.keyDown(key='right')
time.sleep(1.2)
pydirectinput.keyUp(key='space')
pydirectinput.keyUp(key='right')


pydirectinput.keyDown(key='right')
time.sleep(.2)
pydirectinput.keyDown(key='space')
time.sleep(.1)
pydirectinput.keyUp(key='space')
time.sleep(.2)
pydirectinput.keyUp(key='right')

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