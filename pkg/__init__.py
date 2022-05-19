import requests

with open("temp.txt", "w") as f:
    f.write(requests.get("https://www.yahoo.co.jp").content.decode())
