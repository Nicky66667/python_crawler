### 1. Learn_urllib

urllib: To fetch internet resources

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

### 2. learn requests

requests is the strong library which needs less code to imitate browser.

- get(url, params, args)
- delete(url, args)
- post(url, data, json, args)
- request(method, url, args)

### 3. crawl_douban

**For some website, it is needed to mimic a browser request. So we need a user-agent element in our header, which can be found in "Network" on chrome.**

This is the example to crawl movie information from douban.
By using regex, get the information by filtering html source code:
- movie name
- score
- number of comment 
- year
Then, store them into csv file.



