"""
    Phân quyền cho danh sách folder trên ổ đĩa remote
"""

import os
import win32security
import ntsecuritycon as con

# Define the base path
base_path = r'\\172.16.0.191\2.0 ksnb\TUAN_AN_GROUP\BAN_KINH_DOANH\QUAN_LY_THAU_01'

# List of folders to deny access to
folders_to_deny = ["24_GOI_THAU_0010_0000", "24_GOI_THAU_0009_0000", "24_GOI_THAU_0008_IB9898767676"]  # Replace with your actual folder names

# Specify the remote machine name
remote_machine = r'\\172.16.0.191'

# Function to get the SID for a user or group
def get_sid(machine, account_name):
    try:
        sid, domain, account_type = win32security.LookupAccountName(machine, account_name)
        return sid
    except Exception as e:
        print(f"Error retrieving SID for {account_name}: {e}")
        return None

# Get SIDs for the accounts
user_sid = get_sid(remote_machine, "long-nguyen")
admin_sid = get_sid("", "Administrators")
deny_user_sid = get_sid(remote_machine, "long-nguyen2")

if not user_sid or not admin_sid or not deny_user_sid:
    print("Failed to retrieve one or more SIDs. Exiting.")
    exit(1)

# Function to set permissions
def set_permissions(folder_path):
    try:
        # Ensure the folder exists
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")

        # Get the security descriptor for the folder
        sd = win32security.GetFileSecurity(folder_path, win32security.DACL_SECURITY_INFORMATION)

        # Create a new DACL
        dacl = win32security.ACL()

        # Add the user with full control
        dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, user_sid)

        # Add the Administrators group with full control
        dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, admin_sid)

        # Deny access to the user "long-nguyen2"
        dacl.AddAccessDeniedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, deny_user_sid)

        # Set the new DACL for the folder
        sd.SetSecurityDescriptorDacl(1, dacl, 0)
        win32security.SetFileSecurity(folder_path, win32security.DACL_SECURITY_INFORMATION, sd)

        print(f"Permissions successfully set for {folder_path}")
    except Exception as e:
        print(f"Error setting permissions for {folder_path}: {e}")

# Loop through each folder and set permissions
for folder in folders_to_deny:
    folder_path = os.path.join(base_path, folder)
    set_permissions(folder_path)
