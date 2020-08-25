import requests
import json

target = "http://172.16.30.101/ins"

username="cisco"
password="cisco"

requestHeaders = {"content-type":"application/json"}

showcmd = {
    "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "show ip interface brief",
    "output_format": "json"
  }
}

response = requests.post(
    target,
    data=json.dumps(showcmd),
    headers=requestHeaders,
    auth=(username,password),
    verify=False,
).json()

print(response.json())
#print(json.dumps(response,indent=2, sort_keys=True))