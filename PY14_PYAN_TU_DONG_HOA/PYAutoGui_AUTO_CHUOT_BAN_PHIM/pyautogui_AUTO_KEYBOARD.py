# pip install pyautogui
# https://www.vniteach.com/2022/07/25/tai-lieu-lap-trinh-tu-dong-voi-pyautogui-trong-python/
# https://pyautogui.readthedocs.io/en/latest/index.html

import pyautogui as pag

#========= các phím nào có thể được nhấn thông qua mã trong pyautogui, cũng như quy ước đặt tên chính xác của chúng
print(pag.KEYBOARD_KEYS)['t', 'n', 'r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-',
                         '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?',
                         '@', '[', '', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{',
                         '|', '}', '~', 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
                         'browserback', 'browserfavorites', 'browserforward', 'browserhome', 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear', 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete', 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja', 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail', 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack', 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn', 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator', 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab', 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen', 'command', 'option', 'optionleft', 'optionright']

#========= Hàm typewrite () nhấn cả các nút theo một trình tự, không nhấn đồng thời
pag.typewrite('Junaid Khalid', 0.2)     # dừng 0.2 giây sau khi gõ mỗi chữ cái
pag.typewrite(['enter'], 0.2)           # ấn phím enter
pag.typewrite(['j', 'u', 'n', 'a', 'i', 'd', 'e', 'backspace', 'enter'], 0.2)   # ấn phím xoá và phím enter

#========= Hàm hotkey () nhấn đồng thời hai hoặc nhiều phím
pag.hotkey('shift', 'enter')
pag.hotkey('shift', 'a' ) # Viết hoa chữ a
pag.hotkey('ctrl', 'c')  # For the copy command

#========= Chức năng chụp màn hình ()
scree_shot = pag.screenshot()   # to store a PIL object containing the image in a variable
pag.screenshot('ss.png')        # Save image with name ss.png

#========= Các hàm xác nhận (), alert () và prompt ()
pag.confirm("Are you ready?")
pag.alert("The program has crashed!")
pag.prompt("Please enter your name: ")