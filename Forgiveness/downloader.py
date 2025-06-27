import requests
import os
import re
from bs4 import BeautifulSoup

#url = "https://ir.lawnet.fordham.edu/trans/"
url = "https://ir.lawnet.fordham.edu/trans/index.2.html"

resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")

pdf_link = soup.find_all("a", href=True, string="PDF")


if pdf_link:
    for link in pdf_link:
        r = re.search(r".*? - (.*?)\)\s", link["aria-label"])
        match = r[1]
        filename = match.replace(r" (", "-")
        filename = filename + ".pdf"
        pdf_url = link["href"]
        pdf_response = requests.get(pdf_url)

        with open(os.path.join("transcripts", filename), "wb") as f:
            f.write(pdf_response.content)
