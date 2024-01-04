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
    extract.append(clean.text)
    #print(clean.text)
  return(extract)

list1 = process('./classes/1.html')
list2 = process('./classes/2.html')

maxl = max(len(list1), len(list2))
minl = min(len(list1), len(list2))


#print("\nClass List comparison side-by-side")
#df = pd.DataFrame({'Class_1': list1, 'Class_2': list2})
#print(df)

print("List of people who attended the same two classes together:")
for person in list1:
  for friend in list2:
    if (person == friend):
      print(person)
