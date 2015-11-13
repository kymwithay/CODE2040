from urllib2 import Request, urlopen, URLError

requests = Request('https://github.com/kymwithay/CODE2040')

try:
	response = urlopen(requests)
	code2040 = response.read()

except URLerror, e:
	print 'Failed Attempt'