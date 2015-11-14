
#CODE2040
#Kymberlee Hill
#Stage One : Reversed String


import requests
import json


token = {'token': 'jJ4uV46FdF' }

getstring_url = 'http://challenge.code2040.org/api/getstring'
send_url = 'http://challenge.code2040.org/api/validatestring'

accessing_server = requests.post(getstring_url, data = json.dumps(token))

jsonData = accessing_server.json()
test_string = jsonData['result']
print test_string
reversString = test_string[::-1]
print reversString

#send new reversed string back

result = {'token': 'jJ4uV46FdF', 'string': reversString}

second_access = requests.post(send_url, data = json.dumps(result))
challenge_results = second_access.json()
print(challenge_results)
