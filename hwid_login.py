import requests
import subprocess
import sys
pastebin = 'your paste bin raw link that has the hwid of the user'
hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
r = requests.get(pastebin)

if hwid in r.text:
    print("Successfully Logged In!!")
    pass
else:
    sys.exit("Login Failure")
