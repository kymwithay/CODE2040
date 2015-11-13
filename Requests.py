from urllib2 import REQUEST, urlopen, URLerror

requests = REQUEST('https://github.com/kymwithay/CODE2040')

try:
	response = urlopen(requests)
	code2040 = response.read()

except URLerror, e:
	print 'Failed Attempt'