# chương trình chào hỏi và yêu cầu nhập thông tin từ người sử dụng
print ("Tên bạn là gì ?") # hỏi tên
myname = input()
print("Rất vui được gặp bạn ", myname)
print ("Tên bạn rất là đẹp")
print ("Tên của bạn có chứa " + str(len(myname)) + " ký tự")

print ("Bạn sinh năm bao nhiêu ?") 
mybithday = input()

print (" Vậy là năm nay bạn đã " + str(2024 - int (mybithday)) + " tuổi")