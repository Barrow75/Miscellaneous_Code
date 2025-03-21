# for data science/machine learning

import pandas as pd

url = "[enter url.csv]"
df = pd.read_csv(url)
print(df)



# simply reading a CSV

import requests
import csv
import io 

# csv file url
url_request = "[enter url.csv]"

# get contents of csv

# .get makes a get request to the URL requesting the file (hey get me this file)
response = requests.get(ur_request)
#b .text gives the entire csv file content as a string
csv_text = response.text

# stringIO treats the text as a file object
csv_file = io.StringIO(csv_text)

# read  csv using csv reader
reader = csv.reader(csv_file)

# loops through each row and prints it
for row in reader:
  print(row)

