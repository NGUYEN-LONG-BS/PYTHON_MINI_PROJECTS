# Bước 1: Cài đặt thư viện cần thiết:
# Nếu bạn chưa cài đặt thư viện cryptography, hãy chạy lệnh sau:
# pip install cryptography


# Bước 2: Tạo một khóa mã hóa
# Chạy đoạn mã sau một lần để tạo một khóa bí mật (encryption_key.key). Khóa này sẽ được sử dụng để mã hóa và giải mã dữ liệu.

from cryptography.fernet import Fernet

# Tạo khóa mã hóa
encryption_key = Fernet.generate_key()

# Lưu khóa vào file để sau này giải mã
with open("encryption_key.key", "wb") as key_file:
    key_file.write(encryption_key)

print("Encryption key generated and saved!")

# Bước 3: Mã hóa thông tin và lưu vào config.json
# Chạy đoạn mã này để mã hóa thông tin đăng nhập và lưu vào file config.json.

import json
from cryptography.fernet import Fernet

# Đọc khóa mã hóa đã tạo trước đó
with open("encryption_key.key", "rb") as key_file:
    encryption_key = key_file.read()

cipher_suite = Fernet(encryption_key)

# Thông tin cần mã hóa
config_data = {
    "DB_HOST": "14.225.xxx.xxx",
    "DB_USER": "xx",
    "DB_PASSWORD": "Ta#xxxx",
    "DB_NAME": "BAN_KINH_xxx"
}

# Mã hóa từng giá trị
encrypted_config = {key: cipher_suite.encrypt(value.encode()).decode() for key, value in config_data.items()}

# Lưu vào file config.json
with open("config.json", "w") as config_file:
    json.dump(encrypted_config, config_file, indent=4)

print("Config file encrypted and saved successfully!")


# Bước 4: Cách giải mã và đọc lại config.json
# Khi cần sử dụng dữ liệu, bạn có thể giải mã chúng như sau:

# Đọc khóa mã hóa
with open("encryption_key.key", "rb") as key_file:
    encryption_key = key_file.read()

cipher_suite = Fernet(encryption_key)

# Đọc dữ liệu từ file config.json
with open("config.json", "r") as config_file:
    encrypted_config = json.load(config_file)

# Giải mã dữ liệu
decrypted_config = {key: cipher_suite.decrypt(value.encode()).decode() for key, value in encrypted_config.items()}

print(decrypted_config)
