#### requirment not necessary

capture package tool: Fiddler

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

**get method example**:
run `requests_get.py`

**post method example**:
run `requests_post.py`

### 3. crawl_douban

This is the example to crawl movie information from douban.

For some website, it is needed to mimic a browser request. So we need a user-agent element in our header, which can be found in "Network" on chrome.

By using regex, get the information by filtering html source code:
- movie name
- score
- number of comment 
- year

Then, store them into csv file.


### 4. Web Rendering and HTTP

Client-Side Rendering (CSR): rendering in the client’s browser.
The web server sends a basic HTML file to the browser, which includes JavaScript code (like a React, Vue.js, or Angular app). The browser (client) then downloads and runs the JavaScript to dynamically build the page's content. 

Server-Side Rendering (SSR): The web server renders the entire HTML for a page and sends it to the browser.
When a user requests a page, the server processes that request, generates the HTML (sometimes with a framework like Next.js or Express for Node.js), and sends it to the client for display.

Request:
1. request method: get/post
2. request header: information
3. request body: parameters

Response:
1. response status: protocol
2. response header: information
3. response body: e.g., html, json

Request header:
1. User_Agent: Identity of request
2. Referer: anti-hotlinking
3. cookie

