#learning request method
import requests

query = input("search something here:")
url = f'https://www.google.com/search?q={query}'

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

x = requests.get(url, headers=header)

print(x.text)
