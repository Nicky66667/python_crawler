# request to fetch sources
# re to filter information
# csv to store filtered data

import requests
import re
import csv

# URL of the website
url = "https://movie.douban.com/top250"

# Header to mimic a browser request to avoid blocking
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

# Send a request to fetch the page's HTML content
request = requests.get(url, headers=header)

# the source of html from original website
content = request.text

# Regex pattern to extract movie name, year, score, and number of reviews
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
                 r'.*?<p class="">.*?<br>(?P<year>.*?)&nbsp'
                 r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                 r'.*?<span>(?P<number>.*?)人评价</span>', re.S)

# Apply the regex to filter information
result = obj.finditer(content)

# Open CSV file to store the filtered data
f = open("data_douban.csv", mode="w", encoding="utf-8")
writer = csv.writer(f)

# Iterate through the filtered data and write to CSV
for item in result:
    print("name: "+item.group("name"))
    print("score: "+item.group("score"))
    print("number of comments: "+item.group("number"))
    print("year: "+item.group("year").strip())
    print("---------------------------")

    # Clean and store the filtered data into the CSV
    dic = item.groupdict()
    dic['year'] = dic['year'].strip()
    writer.writerow(dic.values())

f.close()