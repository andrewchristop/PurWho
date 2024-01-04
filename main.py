import pandas as pd
import bs4 as bs

def process(path):
  html_file_path = path 
  
  # Read the HTML file content
  with open(html_file_path, 'r', encoding='utf-8') as file:
      html_content = file.read()
  
  # Use BeautifulSoup to parse the HTML content
  soup = bs.BeautifulSoup(html_content, 'html.parser')
  
  # Extracts content and saves it to a ResultSet object
  names = soup.find_all("th", {"class": "d_ich d2l-table-cell-first", "scope": "row"})

  extract = []
  
  # Iterates over the ResultSet object and only appends string value (student name) in empty list
  for clean in names:
    extract.append(clean.text)
    #print(clean.text)
  return(extract)

#Function call to process the class email directories
list1 = process('./classes/1.html')
list2 = process('./classes/2.html')

# Calculates highest, lowest, and difference between the number of elements between one classlist and the other
maxl = max(len(list1), len(list2))
minl = min(len(list1), len(list2))
diff = maxl - minl

# Pads empty classlist if one class has more students than the other so Pandas would work with the dataset
if (diff > 0):
  if (minl == len(list1)):
    for i in range(0, diff):
      list1.append("None")
  elif (minl == len(list2)):
    for j in range(0, diff):
      list2.append("None")

# Prints each classlist side-by-side
print("\nClass List comparison side-by-side")
df = pd.DataFrame({'Class_1': list1, 'Class_2': list2})
pd.set_option('display.max_rows', None)
print(df)

# Compares each name from one class with the other and prints the same ones
print("\nList of people who attended the same two classes together:")
for person in list1:
  for friend in list2:
    if (person == friend):
      print(person)
