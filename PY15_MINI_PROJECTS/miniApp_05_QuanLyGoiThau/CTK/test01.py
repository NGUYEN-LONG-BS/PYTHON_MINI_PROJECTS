import winrm

# Thông tin kết nối VPS
hostname = 'http://14.225.207.110:5985/wsman'
username = 'root'
password = 'Ta#9999'

# Tạo session
session = winrm.Session(hostname, auth=(username, password))

# Thực thi lệnh để liệt kê thư mục
result = session.run_cmd('cmd.exe /c "dir D:\\ /AD"')

# In kết quả
print(result.std_out.decode())
print(result.std_err.decode())