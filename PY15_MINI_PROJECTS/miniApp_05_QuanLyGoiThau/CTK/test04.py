import os
import win32security
import win32api
import ntsecuritycon as con
import pywintypes

# Define the folder path
folder_path = r'\\172.16.0.191\2.0 ksnb\TUAN_AN_GROUP\BAN_KINH_DOANH\QUAN_LY_THAU_01\folder_number_02'

# Ensure the folder exists
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

try:
    # Get the security descriptor for the folder
    sd = win32security.GetFileSecurity(folder_path, win32security.DACL_SECURITY_INFORMATION)
    print("Successfully retrieved security descriptor.")

    # Create a new DACL
    dacl = win32security.ACL()

    # Get the SID for the users
    try:
        # Replace 'long-nguyen', 'Administrators', and 'long-nguyen2' with the actual usernames
        user, domain, type = win32security.LookupAccountName(r'\\172.16.0.191', "long-nguyen")
        admin, domain, type = win32security.LookupAccountName(r'\\172.16.0.191', "Administrators")
        deny_user, domain, type = win32security.LookupAccountName(r'\\172.16.0.191', "long-nguyen2")
        print("User accounts resolved successfully.")
    except pywintypes.error as e:
        print(f"Error resolving user accounts: {e}")
        raise

    # Add ACEs to the DACL
    dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, user)
    dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, admin)
    dacl.AddAccessDeniedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, deny_user)
    print("DACL successfully created.")

    # Set the ownership of the folder to the current user
    current_user = win32security.GetTokenInformation(
        win32security.OpenProcessToken(win32api.GetCurrentProcess(), win32security.TOKEN_READ),
        win32security.TokenUser
    )[0]

    # Set ownership in the security descriptor
    sd.SetSecurityDescriptorOwner(current_user, False)
    win32security.SetFileSecurity(folder_path, win32security.OWNER_SECURITY_INFORMATION, sd)
    print("Ownership successfully set.")

    # Apply the new DACL to the folder
    sd.SetSecurityDescriptorDacl(1, dacl, 0)
    win32security.SetFileSecurity(folder_path, win32security.DACL_SECURITY_INFORMATION, sd)
    print(f"Permissions successfully set for {folder_path}")

except pywintypes.error as e:
    print(f"An error occurred: {e}")
