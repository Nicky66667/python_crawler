import urllib.request

# to request resources from baidu and print the output
response = urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))

