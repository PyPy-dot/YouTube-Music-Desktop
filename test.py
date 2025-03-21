import json


file_path = "E:/YouTube Music/cookies.json"

with open(file_path, "r") as f:
    cookies = json.load(f)
    print(cookies)