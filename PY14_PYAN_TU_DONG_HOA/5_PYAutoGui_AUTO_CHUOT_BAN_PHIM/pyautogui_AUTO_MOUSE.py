# pip install pyautogui

import pyautogui as pag

#===============================================================================================================
#========= Print the size of my screen
#===============================================================================================================
size = pag.size()
print(size)

#===============================================================================================================
#========= Print vi tri hien tai cua chuot
#===============================================================================================================
pos = pag.position()
print (pos)

#===============================================================================================================
#========= Hàm onScreen () cho chúng tôi biết liệu điểm có tọa độ x và y có tồn tại trên màn hình hay không
#===============================================================================================================
print(pag.onScreen(500, 600))       # True
print(pag.onScreen(0, 10000))       # FalseJunaid 

#===============================================================================================================
#========= Hàm moveTo ()    Di chuyển chuột so với vị trí (0,0)
#===============================================================================================================
pag.FAILSAFE = False                # Tắt tính năng an toàn không hoạt động, để không bị lỗi chỗ pag.PAUSE = 2
pag.PAUSE = 2                       # Dừng chương trình để thấy con trỏ chuột di chuyển
pag.moveTo(0, 0, duration=2)
pag.PAUSE = 2
pag.moveTo(100, 500, duration=2)
pag.PAUSE = 2
pag.moveTo(500, 500, duration=2)

#===============================================================================================================
#========= Hàm moveRel ()   Di chuyển chuột so với vị trí hiện tại
#===============================================================================================================
print(pag.position())
pag.moveRel(100, 100, 2)
print(pag.position())
pag.moveRel(100, 100, duration=3)
print(pag.position())

#===============================================================================================================
#========= Hàm click ()
#===============================================================================================================

# Auto click
pag.click()
pag.click(x=263, y=18)

# pag.click(x, y, clicks, interval, button)
# Các thông số được giải thích như sau:
# x: tọa độ x của điểm cần tiếp cận
# y: tọa độ y của điểm cần tiếp cận
# clicks: số lần nhấp bạn muốn thực hiện khi con trỏ đến điểm đó trên màn hình
# interval: khoảng thời gian tính bằng giây giữa mỗi lần nhấp chuột, tức là nếu bạn đang thực hiện nhiều lần nhấp chuột
# button: chỉ định nút nào trên chuột bạn muốn nhấn khi con trỏ đến điểm đó trên màn hình. Các giá trị có thể là right, leftvà middle.
pag.click(500, 800, 2, duration=3, button='left')
pag.click(600, 800, 2, duration=3, button='right')
pag.click(x=267, y=10, clicks=2, duration=0, button='left')

pag.FAILSAFE = False
pag.rightClick(x=267, y=10)
pag.PAUSE = 2
pag.doubleClick(x=267, y=10)
pag.PAUSE = 2
pag.tripleClick(x=267, y=10)
pag.PAUSE = 2
pag.middleClick(x=267, y=10)

# Đoạn mã sau tương đương với việc chỉ thực hiện một pag.click(x, y).
pag.mouseDown(x=267, y=10, button='left')
pag.mouseUp(x=267, y=10, button='left')

#===============================================================================================================
#========= Hàm scroll ()
#===============================================================================================================
# pag.scroll(amount_to_scroll, x=x_movement, y=y_movement)

pag.FAILSAFE = False
pag.PAUSE = 2
pag.scroll(190, 120, 120)   # Cuộn lên 190
pag.PAUSE = 2
pag.scroll(-590, 120, 120)   # Cuộn xuống 590

# Dieu chinh thoi gian cho scroll
import time
for s in range(5):              # Lăn chuột n lần
    print(s)
    pag.scroll(-140)             # Một lần lăn chuột, tương ứng với 140
    time.sleep(0.005)           # thời gian nghỉ sau mỗi lần lăn chuột