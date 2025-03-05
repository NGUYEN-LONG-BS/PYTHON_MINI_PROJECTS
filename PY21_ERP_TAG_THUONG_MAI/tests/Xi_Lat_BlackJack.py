import tkinter as tk
from tkinter import messagebox
import random

# Khởi tạo bộ bài
def create_deck():
    return [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

# Tính EV cho lượt rút tiếp theo
def calculate_ev(current_points, deck):
    ev = 0
    for card in deck:
        if current_points + card > 21:
            ev -= 1  # Trường hợp bị bust
        else:
            ev += 1  # Trường hợp cải thiện điểm số
    return ev / len(deck)

# Tính xác suất thắng
def calculate_win_probability(current_points, deck):
    if current_points == 21:
        return 1.0  # Đã thắng với 21 điểm
    win_count = 0
    for card in deck:
        if current_points + card <= 21:
            win_count += 1
    return win_count / len(deck)

# Hàm kiểm tra có nên bốc tiếp không
def should_draw(ev):
    return ev > 0

# Hàm xử lý sau khi nhập bài
class BlackjackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack EV Calculator")

        self.deck = create_deck()
        self.current_points = 0
        self.cards_drawn = []

        # Giao diện nhập bài
        self.entries = []
        for i in range(5):
            label = tk.Label(root, text=f"Nhập giá trị lá bài {i + 1} nhận được (2-11):")
            label.pack()

            entry = tk.Entry(root)
            entry.pack()
            self.entries.append(entry)

        self.calculate_button = tk.Button(root, text="Tính toán sau 2 lá đầu", command=self.calculate_ev_for_first_two)
        self.calculate_button.pack()

        self.result_label = tk.Label(root, text="", fg="blue")
        self.result_label.pack()

    def calculate_ev_for_first_two(self):
        try:
            self.current_points = 0
            self.cards_drawn = []

            for i in range(2):
                card = int(self.entries[i].get())
                if card not in range(2, 12):
                    raise ValueError("Lá bài phải từ 2 đến 11.")

                # Nếu là 11 và tổng điểm > 21, chuyển thành 1
                if card == 11 and self.current_points + card > 21:
                    card = 1

                self.cards_drawn.append(card)
                self.current_points += card

            # Tính EV và xác suất thắng sau 2 lá đầu
            ev = calculate_ev(self.current_points, self.deck)
            win_prob = calculate_win_probability(self.current_points, self.deck)

            # Hiển thị kết quả sau 2 lá đầu
            decision = "Nên bốc thêm" if should_draw(ev) else "Không nên bốc thêm"
            self.result_label.config(text=f"Điểm hiện tại: {self.current_points}\nEV: {ev:.2f}\nXác suất thắng: {win_prob:.2%}\nQuyết định: {decision}")

            # Cập nhật bộ bài (loại bỏ 2 lá bài đầu tiên)
            for card in self.cards_drawn:
                if card in self.deck:
                    self.deck.remove(card)

            # Kiểm tra các entries tiếp theo nếu có giá trị
            for i in range(2, 5):
                card_text = self.entries[i].get()
                if card_text:
                    card = int(card_text)
                    if card not in range(2, 12):
                        raise ValueError("Lá bài phải từ 2 đến 11.")

                    # Nếu là 11 và tổng điểm > 21, chuyển thành 1
                    if card == 11 and self.current_points + card > 21:
                        card = 1

                    self.cards_drawn.append(card)
                    self.current_points += card

                    ev = calculate_ev(self.current_points, self.deck)
                    win_prob = calculate_win_probability(self.current_points, self.deck)
                    decision = "Nên bốc thêm" if should_draw(ev) else "Không nên bốc thêm"
                    self.result_label.config(text=f"Điểm hiện tại: {self.current_points}\nEV: {ev:.2f}\nXác suất thắng: {win_prob:.2%}\nQuyết định: {decision}")

                    if card in self.deck:
                        self.deck.remove(card)

        except ValueError as e:
            messagebox.showerror("Lỗi", str(e))

# Chạy ứng dụng
if __name__ == "__main__":
    root = tk.Tk()
    app = BlackjackApp(root)
    root.mainloop()
