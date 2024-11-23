# ======================================================================================
# Dowloading dữ liệu từ web với Request
# Lưu file ở path hiện hành
# ======================================================================================
import requests

down_url = "https://facebook.com/favicon.ico"

def Function_Down_File(linkDown, fileName):
    req = requests.get(linkDown)
    with open(fileName, "wb") as f:
        f.write(req.content)
        
Function_Down_File(down_url,"faceBook.ico")

# ======================================================================================
# Lưu file ở path tự chọn
# ======================================================================================
import requests
import os

down_url = "https://facebook.com/favicon.ico"

def Function_Down_File(linkDown, fileName, savePath):
    # Ensure the save path directory exists
    os.makedirs(savePath, exist_ok=True)
    
    # Combine the path and filename
    full_path = os.path.join(savePath, fileName)
    
    # Request the file and save it
    req = requests.get(linkDown)
    with open(full_path, "wb") as f:
        f.write(req.content)
    print(f"File saved at: {full_path}")

# Example usage
Function_Down_File(down_url, "faceBook.ico", r"C:\Users\ADMIN\Desktop")