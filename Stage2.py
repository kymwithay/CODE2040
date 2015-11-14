#Code2040
#Kymberlee Hill
#Stage Two: Haystack

import requests
import json

token = {'token': 'jJ4uV46FdF' }

get_url = 'http://challenge.code2040.org/api/haystack'
send_url = 'http://challenge.code2040.org/api/validateneedle'

accessing_server = requests.post(get_url, data = json.dumps(token))

jsonData = accessing_server.json()

haystack = jsonData['result']['haystack']
needle = jsonData['result']['needle']

print "watch out for the needle:" + " " + needle + " " + "in the given haystack"

length = len(haystack) - 1

for index in xrange(length):
	print haystack[index]
	if haystack[index] == needle:
		location = index
		print index

result2 = {'token': 'jJ4uV46FdF', 'needle': location}

second_access2 = requests.post(send_url, data = json.dumps(result2))
challenge_results = second_access2.json()
print(challenge_results)
