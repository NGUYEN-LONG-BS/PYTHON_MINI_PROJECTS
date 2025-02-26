import matplotlib.pyplot as plt

# Dữ liệu mẫu
categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
values = [20, 35, 30, 35, 27]

# Vẽ biểu đồ cột ngang
plt.barh(categories, values, height=0.5)

# Thêm tiêu đề và nhãn
plt.title('Horizontal Bar Chart Example')
plt.xlabel('Values')
plt.ylabel('Categories')

# Hiển thị biểu đồ
plt.show()
