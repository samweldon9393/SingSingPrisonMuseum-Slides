import requests
from bs4 import BeautifulSoup
import json

base = "https://ir.lawnet.fordham.edu/trans/"

for i in range(1, 201):
    url = base + str(i)

    response = requests.get(url)

    print(response.status_code)
    if response.status_code != 200:
        print("Failed to get url")
