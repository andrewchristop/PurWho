import pandas as pd
import bs4 as bs

def process(path):
  html_file_path = path 
  
  # Read the HTML file content
  with open(html_file_path, 'r', encoding='utf-8') as file:
      html_content = file.read()
  
  # Use BeautifulSoup to parse the HTML content
  soup = bs.BeautifulSoup(html_content, 'html.parser')
  #results = soup.find(id="z_l")
  
  names = soup.find_all("th", {"class": "d_ich d2l-table-cell-first", "scope": "row"})

  extract = []
  
  for clean in names:
    print(clean.text)

process('./classes/2.html')
