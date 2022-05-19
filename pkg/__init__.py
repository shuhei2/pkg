import requests

with open("temp.txt", "w", encoding="utf-8") as f:
    f.write(requests.get("https://www.yahoo.co.jp").content.decode())
