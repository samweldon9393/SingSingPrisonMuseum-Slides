import requests
from bs4 import BeautifulSoup
import json

base = "https://ir.lawnet.fordham.edu/trans/"
url = base + "1"
response = requests.get(url)

html = response.text
soup = BeautifulSoup(html, "html.parser")

alpha = soup.body.find(id="alpha")

for child in alpha.children:
    for s in child.strings:
        print(s)
        ''' printing 3 blank lines in between, can we delimit with that? '''


'''
for i in range(1, 201):
    url = base + str(i)

    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to get url")
'''
