import json
import requests

URL = "http://192.168.0.105:8080/hackathon/basf/ingredients"
headers = {'content-type':'application/json','Accept':'application/json'}
# data = result_text.json()
data_raw = ['blah','blah']
data = json.dumps(data_raw)
print(data)
requests.post(url=URL,data=data,headers=headers)