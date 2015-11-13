import requests
import json

#JSON DICTIONARY
{
	"body": {
		"Email": "hillkymberlee@gmail.com",
		 "github": "https://github.com/kymwithay/CODE2040"
		 }
}
#Makes the POST REQUEST here, passing body in as the data:
response = requests.POST("http://challenge.code2040.org/api/register", data = body)
