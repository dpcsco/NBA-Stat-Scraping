from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import time
from io import StringIO


months = ["https://www.basketball-reference.com/leagues/NBA_2025_games-october.html",
          "https://www.basketball-reference.com/leagues/NBA_2025_games-november.html",
          "https://www.basketball-reference.com/leagues/NBA_2025_games-december.html",
          "https://www.basketball-reference.com/leagues/NBA_2025_games-january.html",
          "https://www.basketball-reference.com/leagues/NBA_2025_games-february.html"
]
          
base_url = "https://basketball-reference.com"

all_bs_urls = []


start_time = time.perf_counter()

def locate_box(url):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    box_score_table = doc.find("table")
    body = box_score_table.find("tbody")
    box_score_items = body.find_all(string="Box Score")

    return box_score_items

def create_urls(bs_items):
    month_urls = [base_url + element.parent.get('href') for element in bs_items]
    return month_urls

def main():
    all_bs_urls = [create_urls(locate_box(link)) for link in months]
    print(all_bs_urls)

if __name__ == "__main__":
    main()

#TIME COUNT
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")