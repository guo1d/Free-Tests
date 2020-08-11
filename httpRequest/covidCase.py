import requests
import json

URL = "https://service-f9fjwngp-1252021671.bj.apigw.tencentcs.com/release/pneumonia"

r = requests.get(url = URL)

data = r.json() 

json_data = json.loads(r.text)

print(json_data['data']['statistics'])
