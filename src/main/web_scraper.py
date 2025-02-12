from bs4 import BeautifulSoup
import requests
import re

#with open("index.html", "r") as f:
    #doc = BeautifulSoup(f, "html.parser")


url = "https://www.nba.com/stats/players/boxscores"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

test = doc.find_all(["span", "th", "div"], string=re.compile("OREB", re.IGNORECASE))
print(test)
#parent = test[0].parent
#print(parent)