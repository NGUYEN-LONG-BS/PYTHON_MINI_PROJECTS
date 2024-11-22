"""
    Phân quyền folder trên ổ đĩa remote
"""

import win32net
import win32netcon

# ======================================================================================
# FUNC_LIST_USERS_AT_MYCOMPUTER
# ======================================================================================
def FUNC_LIST_USERS_AT_MYCOMPUTER():
    resume = 0
    user_list = []
    while True:
        users, total, resume = win32net.NetUserEnum(None, 0, win32netcon.FILTER_NORMAL_ACCOUNT, resume)
        user_list.extend([user['name'] for user in users])
        if not resume:
            break
    return user_list

print(FUNC_LIST_USERS_AT_MYCOMPUTER())

# ======================================================================================
# FUNC_LIST_USERS_AT_REMOTE_IP
# ======================================================================================
def FUNC_LIST_USERS_AT_REMOTE_IP(remote_machine):
    resume = 0
    user_list = []
    while True:
        users, total, resume = win32net.NetUserEnum(remote_machine, 0, win32netcon.FILTER_NORMAL_ACCOUNT, resume)
        user_list.extend([user['name'] for user in users])
        if not resume:
            break
    return user_list

# Specify the remote machine's IP address
remote_machine = r'\\172.16.0.191'

print(FUNC_LIST_USERS_AT_REMOTE_IP(remote_machine))

# ======================================================================================
# CREATE FOLDER AND CHANGE PERMISSIONS
# ======================================================================================
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

# Specify the remote machine name
remote_machine = r'\\172.16.0.191'

# Get the SID for the user (replace 'username' with the actual username)
user, domain, type = win32security.LookupAccountName(remote_machine, "long-nguyen")
admin, domain, type = win32security.LookupAccountName("", "Administrators")
deny_user, domain, type = win32security.LookupAccountName(remote_machine, "long-nguyen2")

# Add the user with full control
dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, user)

# Add the Administrators group with full control
dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, admin)

# Deny access to the user "long-nguyen2"
dacl.AddAccessDeniedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, deny_user)

# Set the new DACL for the folder
sd.SetSecurityDescriptorDacl(1, dacl, 0)
win32security.SetFileSecurity(folder_path, win32security.DACL_SECURITY_INFORMATION, sd)

print(f"Permissions set for {folder_path}")