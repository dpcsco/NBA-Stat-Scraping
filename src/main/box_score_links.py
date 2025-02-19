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
          #Add additional months as needed
]
          
base_url = "https://basketball-reference.com"

start_time = time.perf_counter()


#BeautifulSoup scrapes the url for a given page and returns a list of Box Score elements
def locate_box(url):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    box_score_table = doc.find("table")
    body = box_score_table.find("tbody")
    box_score_items = body.find_all(string="Box Score")

    return box_score_items

#takes in a list of Box Score elements and makes a list of urls for each
def create_urls(bs_items):
    month_urls = [base_url + element.parent.get('href') for element in bs_items]
    return month_urls

#creates a nested list of every month's list of urls
def gen_list_links():
    all_bs_urls = [create_urls(locate_box(link)) for link in months]
    return all_bs_urls

if __name__ == "__main__":
    print(gen_list_links())

#TIME COUNT
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")