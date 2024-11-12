from ahk import AHK

ahk = AHK()

# Di chuyển chuột đến vị trí (100, 100)
ahk.mouse_move(x=100, y=100, blocking=True)

# Thiết lập phím nóng để hiển thị thông báo
def show_message():
# ahk.message_box("Hello from Python!")

# ahk.add_hotkey('F1', callback=show_message)
# ahk.start_hotkeys()