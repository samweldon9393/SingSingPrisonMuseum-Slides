import requests
import os
from bs4 import BeautifulSoup

url = "https://ir.lawnet.fordham.edu/trans/"

resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")

pdf_link = soup.find_all("a", href=True, string="PDF")

print(len(pdf_link))
