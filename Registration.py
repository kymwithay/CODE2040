#Code2040
#Kymberlee Hill

import requests
import json

#ALL REQUIRED URLS
register_url = 'http://challenge.code2040.org/api/register'

getstring_url = 'http://challenge.code2040.org/api/getstring'
send_reversedstring_url= 'http://challenge.code2040.org/api/validatestring'

getHaystack_url = 'http://challenge.code2040.org/api/haystack'
sendHaystack_url = 'http://challenge.code2040.org/api/validateneedle'

getPrefix_url = 'http://challenge.code2040.org/api/prefix'
sendPrefix_url = 'http://challenge.code2040.org/api/validateprefix'

getDate_url = 'http://challenge.code2040.org/api/time'
sendDate_url = 'http://challenge.code2040.org/api/validatetime'

#def getToken():

#JSON Dictionary
body = {
    'email': 'hillkymberlee@gmail.com',
    'github': 'https://github.com/kymwithay/CODE2040'
  }
#Makes the POST REQUEST here, passing body in as the data:
response = requests.post(register_url, data=json.dumps(body))
jsonData = response.json()
result = jsonData['response']
print result

###### This function expects a sting and will return the reversed string

#def stageOne(token):
  #body = {
   # 'token': 'token'
  #}

  #Makes POST REQUEST here, passing in body as the data
  #response = requests.post('getstring_url', data = json.dumps(body))
  #jsonData = response.json()
  #test_string = jsonData['result']

  #
 # return {'token': token, 'string': reverseString}



#######

#def main():
  #token = getToken()
 # stageOne(token)


#if __name__ == '__main__':
#  main()
