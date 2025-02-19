from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import time
from io import StringIO
import box_score_links
from requests_ratelimiter import LimiterSession


#url = "https://www.basketball-reference.com/boxscores/202410220LAL.html"

start_time = time.perf_counter()

session = LimiterSession(per_minute=10)

#takes in a url and uses pandas to read the html

def read_box(url):
    result = session.get(url)
    dfs = pd.read_html(StringIO(result.text))
    print(dfs[0])


def main():
    test_list = box_score_links.gen_list_links()

    for month in test_list[0]:
        #for element in month[:10]:
        test_month = month[:5]
        read_box(test_month)
            #read_box(element)

if __name__ == "__main__":
    main()

'''''
result = requests.get(url)
dfs = pd.read_html(StringIO(result.text))
'''''
#twolves = dfs[0]

#print(twolves.iloc[:, [0,19]])

end_time = time.perf_counter()

execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")