# reading and writing to CSV manually 

import csv

# writing to CSV 
with open("example.csv", "w", newline="") as file:
  writer = csv.writer(file)
  writer.writerow(["name", "age", "country"])
  writer.writerow(["Alice", 25, "USA"])
  writer.writerow(["Bob", 30, "UK"])


# reading CSV file
with open("example.csv", "r") as file:
  reader = csv.reader(file)
  for row in reader:
    print(row)
