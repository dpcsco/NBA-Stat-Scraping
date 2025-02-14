from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import time
from io import StringIO


url = "https://www.basketball-reference.com/boxscores/202410220LAL.html"



start_time = time.perf_counter()

#dfs = pd.read_html("https://www.basketball-reference.com/boxscores/202410220BOS.html")

#print(dfs[0])

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

#test = doc.find_all("table")
dfs = pd.read_html(StringIO(result.text))


twolves = dfs[0]

print(twolves.iloc[:, [0,19]])
#print(dfs[8].iloc[[1,0]])




#BRANCH_BY_BRANCH
#test2 = doc.find("div", class_="table_container", id="div_box-NYK-game-basic")
#test2 = doc.find_all("tr")
#test3 = test2.find("table")

#DATAFRAMES
#df = pd.DataFrame(test3)
#print(df)


#TESTS
#test3 = test2.find("tbody")
#test4 = test3.find_all("tr")


#PRINTLINES
#print(len(test3))
#print(test2)
#print(test4[0].prettify())
#print(test4[1].prettify())


end_time = time.perf_counter()

execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")