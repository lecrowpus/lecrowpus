import pyautogui
import requests
import json
url = "http://127.0.0.1:5000/"

response =requests.request("GET", url)
response=json.loads(response.text) 
pyautogui.moveTo(int(response["x"]), int(response["y"]))

# print(json.loads(response.text))