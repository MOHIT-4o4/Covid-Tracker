import os
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
from prettytable import PrettyTable


# Step 1: Sending a HTTP request to a URL
url = "https://www.mohfw.gov.in/"
# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text
print("Web Scrapping has begun...")

# Step 2: Parse the html content
soup = BeautifulSoup(html_content, "lxml")
# soup.p.get_attribute_list("marquee")
soup.find_all('<a href="/covid/">COVID-19 Dashboard</a>')
extract_contents = lambda row: [x.text.replace('\n', '') for x in row]
# print(soup.prettify()) # print the parsed data of html
# for url in soup.find_all("a"):
    # print("Title:{}".format(url.get("title")))

stats = []
# all_rows = soup.find('statecount')
# for i in stats:
#     stats.append(all_rows)

for _ in stats:
    stat = extract_contents(soup.find_all('<a href="/covid/">COVID-19 Dashboard</a>'))
print(soup.text)
#     if len(stat)==5:  #for 10 lines
#         stats.append(stat)
# colm = ["Sr.No", "States/UT","Confirmed","Recovered","Deceased"]

# state_data = pd.DataFrame(data=stats,columns=colm)
# state_data.head()
# table = PrettyTable()
# table.field_names = (colm)
# 
#     table.add_row(["","Total", 
#                sum(state_data["Confirmed"]), 
#                sum(state_data["Recovered"]),
#                sum(state_data["Deceased"])])
# print(table)