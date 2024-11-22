# Tạo thư mục mới và phân quyền cho thư mục

import os
import win32security
import ntsecuritycon as con

# Define the folder path
folder_path = r'\\172.16.0.191\2.0 ksnb\TUAN_AN_GROUP\BAN_KINH_DOANH\QUAN_LY_THAU_01\folder_number_02'

# Ensure the folder exists
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Get the security descriptor for the folder
sd = win32security.GetFileSecurity(folder_path, win32security.DACL_SECURITY_INFORMATION)

# Create a new DACL
dacl = win32security.ACL()

# Get the SID for the user (replace 'username' with the actual username)
user, domain, type = win32security.LookupAccountName("", "MYDOMAIN\\long-nguyen")
admin, domain, type = win32security.LookupAccountName("", "Administrators")

# Add the user with full control
dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, user)

# Add the Administrators group with full control
dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, admin)

# Set the new DACL for the folder
sd.SetSecurityDescriptorDacl(1, dacl, 0)
win32security.SetFileSecurity(folder_path, win32security.DACL_SECURITY_INFORMATION, sd)

print(f"Permissions set for {folder_path}")