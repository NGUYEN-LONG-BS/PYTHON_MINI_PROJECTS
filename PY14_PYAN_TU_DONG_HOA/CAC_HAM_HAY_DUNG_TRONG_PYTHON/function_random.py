import random

# Hàm random() trả về một số thực ngẫu nhiên trong khoảng [0.0, 1.0).
print(random.random())

# Hàm randint(a, b) trả về một số nguyên ngẫu nhiên N sao cho a <= N <= b.
print(random.randint(1, 10))

# Hàm uniform(a, b) trả về một số thực ngẫu nhiên N sao cho a <= N <= b.
print(random.uniform(1.0, 10.0))

# Hàm randrange(start, stop[, step]) trả về một số nguyên ngẫu nhiên từ dãy số range(start, stop, step).
print(random.randrange(1, 10, 2))  # Số lẻ từ 1 đến 9

# Hàm choice(seq) trả về một phần tử ngẫu nhiên từ chuỗi seq (có thể là danh sách, tuple, hay chuỗi ký tự).
choices = ['apple', 'banana', 'cherry']
print(random.choice(choices))

# Hàm shuffle(x) xáo trộn ngẫu nhiên các phần tử trong danh sách x.
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

# Hàm sample(population, k) trả về một danh sách gồm k phần tử được chọn ngẫu nhiên từ population, không trùng lặp.
numbers = [1, 2, 3, 4, 5]
print(random.sample(numbers, 3))

# Ví dụ về sử dụng Seed
random.seed(42)
print(random.random())
print(random.random())

random.seed(42)         
print(random.random())  # random này sẽ ra kết quả giống random ở trên
print(random.random())  # random này sẽ ra kết quả giống random ở trên