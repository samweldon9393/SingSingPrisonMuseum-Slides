import requests
from bs4 import BeautifulSoup
import json

base = "https://ir.lawnet.fordham.edu/trans/"

tot_map = {}

for i in range(1, 201):
    url = base + str(i)

    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to get url")

    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    alpha = soup.body.find(id="alpha")

    ind_map = {}

    for h2 in alpha.find_all("h2"):
        ind_map[h2.string] = h2.next_sibling.next_sibling.string

    tot_map[i] = ind_map


with open("data.json", "w") as f:
    json.dump(tot_map, f, indent=4)
