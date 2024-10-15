import requests

url = "https://fanyi.baidu.com/sug"

word = input("input something here to translate:")
data = {
    "kw": word
}

x = requests.post(url, data=data)
print(x.json())
x.close()