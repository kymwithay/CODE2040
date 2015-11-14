#Code2040
#Kymberlee Hill
#Stage Four: Dating Game

import requests
import dateutil.parser
import datetime
import iso8601
import json

token = {'token': 'jJ4uV46FdF' }

get_url = 'http://challenge.code2040.org/api/time'
send_url = 'http://challenge.code2040.org/api/validatetime'

accessing_server = requests.post(get_url, data = json.dumps(token))
jsonData = accessing_server.json()
datestamp = jsonData['result']['datestamp']
sec_intervals = jsonData['result']['interval']

converted_sec_intervals = int(sec_intervals)

new_date = iso8601.parse_date(datestamp)

converted_sec_intervals = datetime.timedelta(0, converted_sec_intervals)

date_and_time = new_date + converted_sec_intervals

date_and_time = date_and_time.isoformat()
	
formated_date = date_and_time.split('+')[0]
formated_date += '.000Z'
print formated_date 

result4 = {'token': 'jJ4uV46FdF', 'datestamp': formated_date}
second_access = requests.post(send_url, data = json.dumps(result4))
challenge_results = second_access.json()
print(challenge_results)
