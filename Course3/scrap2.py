import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_English_monarchs"

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

cells = soup.select("table.wikitable tbody tr td:nth-child(1)")

for cell in cells:
    b = cell.find("b").find("a")
    if b != None:
        print(b.text)
    
    i = cell.find("i")
    if i != None:
        print(i.text)