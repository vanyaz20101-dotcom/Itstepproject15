import requests

from bs4 import BeautifulSoup

url = "http://books.toscrape.com"


response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
html = response.text
books = soup.find_all("article", class_="product_pod")

for book in books:
    h3 = book.find("h3")
    a = h3.find("a")
    title = a["title"]
    print(title)