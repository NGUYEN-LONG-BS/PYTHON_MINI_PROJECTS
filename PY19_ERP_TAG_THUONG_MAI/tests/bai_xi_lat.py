import tkinter as tk
from tkinter import messagebox
import random

# Khởi tạo bộ bài
def create_deck():
    return [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

# Tính xác suất thắng
def calculate_win_probability(player_cards, deck):
    player_points = sum(player_cards)
    if player_points == 21:
        return 1.0  # Đã thắng với 21 điểm

    trials = 10000
    win_count = 0

    for _ in range(trials):
        current_deck = deck[:]
        for card in player_cards:
            current_deck.remove(card)
        random.shuffle(current_deck)

        dealer_points = 0
        while dealer_points < 17:
            card = current_deck.pop()
            if card == 11 and dealer_points + card > 21:
                card = 1
            dealer_points += card

        if dealer_points > 21 or player_points > dealer_points:
            win_count += 1

    return win_count / trials

# Hàm xử lý sau khi nhập bài
class BlackjackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack Win Probability Calculator")

        self.deck = create_deck()

        # Giao diện nhập bài
        self.entries = []
        for i in range(5):
            label = tk.Label(root, text=f"Nhập giá trị lá bài {i + 1} nhận được (2-11):")
            label.pack()

            entry = tk.Entry(root, state="normal" if i < 2 else "disabled")
            entry.pack()
            self.entries.append(entry)

        self.calculate_button = tk.Button(root, text="Tính xác suất thắng", command=self.calculate_win_probability)
        self.calculate_button.pack()

        self.result_label = tk.Label(root, text="", fg="blue")
        self.result_label.pack()

    def enable_additional_entries(self, current_count):
        if current_count >= 2 and current_count < 3:
            self.entries[2].config(state="normal")
        if current_count >= 3 and current_count < 4:
            self.entries[3].config(state="normal")
        if current_count >= 4:
            self.entries[4].config(state="normal")

    def calculate_win_probability(self):
        try:
            player_cards = []

            for i, entry in enumerate(self.entries):
                card_text = entry.get()
                if card_text:
                    card = int(card_text)
                    if card not in range(2, 12):
                        raise ValueError("Lá bài phải từ 2 đến 11.")
                    player_cards.append(card)

            if len(player_cards) < 2:
                raise ValueError("Cần nhập tối thiểu 2 lá bài.")

            self.enable_additional_entries(len(player_cards))

            total_points = sum(player_cards)
            win_prob = calculate_win_probability(player_cards, self.deck)
            self.result_label.config(text=f"Tổng điểm: {total_points}\nXác suất thắng: {win_prob:.2%}")

        except ValueError as e:
            messagebox.showerror("Lỗi", str(e))

# Chạy ứng dụng
if __name__ == "__main__":
    root = tk.Tk()
    app = BlackjackApp(root)
    root.mainloop()
