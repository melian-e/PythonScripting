import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.fr/s?k=programming+books"

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

print(soup.prettify())