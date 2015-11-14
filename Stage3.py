#Code2040
#Kymberlee Hill
#Stage Two: Haystack

import requests
import json

token = {'token': 'jJ4uV46FdF' }

get_url = 'http://challenge.code2040.org/api/prefix'
send_url = 'http://challenge.code2040.org/api/validateprefix'

accessing_server3 = requests.post(get_url, data = json.dumps(token))

jsonData = accessing_server3.json()

prefix = jsonData['result']['prefix']
str_array= jsonData['result']['array']

print "prefix is" + " " + prefix

def remove_pre(prefix, str_array):
    new_array = []
    for i in xrange(len(str_array)):
		if str_array[i][0:3]!= prefix:
         		new_array.append(str_array[i])
    return new_array

updated_array = remove_pre(prefix, str_array)

#package and send back
result3 = {'token': 'jJ4uV46FdF', 'array': updated_array}
second_access = requests.post(send_url, data = json.dumps(result3))
challenge_results = second_access.json()
print(challenge_results)