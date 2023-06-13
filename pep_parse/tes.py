import requests
from bs4 import BeautifulSoup

response = requests.get("https://peps.python.org/pep-0001/")
soup = BeautifulSoup(response.text, "lxml")
strin = soup.find("h1", {"class": "page-title"}).text.split()
number = strin[1]
name = strin[4:]
status = soup.find("abbr").text
_, number, _, _, *name = soup.find("h1", {"class": "page-title"}).text.split()

print(" ".join(number))
