#### requirment

capture package tool: Fiddler

### 1. Learn_Urllib

Urllib: To fetch internet resources

1. request: to request
2. error: to handle error
3. parse: to parse URL or domain
4. robotparser: to parse website's robot.txt

**'urlopen' method**: 

default: To request html resources from website
when it has data parameter, it becomes post request

`urllib.request.urlopen(url, data=None, [timeout,]*)`
- url is the link
- data is the parameter for POST request, e.g., the username and password
- timeout is the timeout of request

**'Request' method**: 

- custom request method
- add information in header

`urllib.request.Request(url,data=None, header={}, method=None)`