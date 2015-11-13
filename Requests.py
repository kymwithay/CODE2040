from urllib2 import Request, urlopen, URLError

requests = Request('http://challenge.code2040.org/api/register')

try:
	response = urlopen(requests)
	code2040 = response.read()

except URLerror, e:
	print 'Failed Attempt'