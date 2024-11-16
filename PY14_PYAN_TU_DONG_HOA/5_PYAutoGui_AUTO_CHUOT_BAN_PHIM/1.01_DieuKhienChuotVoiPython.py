# pip install pyautogui

import pyautogui

#========= Print the size of my screen
size = pyautogui.size()
print(size)
w, h = size

#========= Print vi tri hien tai cua chuot
pos = pyautogui.position()
print (pos)

#========= Di chuyển chuột đến vị trí định sẵn
pyautogui.moveTo(500,600, duration=2)

#========= Auto click
pyautogui.click()
pyautogui.click(x=263, y=18)

#========= Tu dong dieu khien chuot ve hinh tren paint
distance = 300
while distance > 0:
    print (distance)
    pyautogui.dragRel (distance, 0, duration= 0.5)
    distance = distance -25
    print (distance)
    pyautogui.dragRel(0, distance, duration= 0.5)
    distance = distance -25
    print (distance)
    pyautogui.dragRel(-distance, 0, duration= 0.5)
    distance = distance -25
    print (distance)
    pyautogui.dragRel(0,-distance, duration= 0.5)
    distance = distance -25
