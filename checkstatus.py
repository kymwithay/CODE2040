#CODE2040
#Kymberlee Hill

import requests  
import json

token = {'token':'jJ4uV46FdF'}
status_url = 'http://challenge.code2040.org/api/status'

accessing_server = requests.post(status_url, data=json.dumps(token))
jsonData = accessing_server.json()

print(jsonData)