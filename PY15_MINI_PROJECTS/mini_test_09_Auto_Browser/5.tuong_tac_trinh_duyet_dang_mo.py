import subprocess

# Define the command
command = r'"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\AutoBrowsers\nguyenlongbshop"'

# Execute the command
subprocess.run(command, shell=True)
