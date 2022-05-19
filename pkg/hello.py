import requests

def hello():
    print(requests.get("https://www.yahoo.co.jp").content)




