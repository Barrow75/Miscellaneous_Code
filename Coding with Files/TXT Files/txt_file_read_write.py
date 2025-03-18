# writing to a file manually

with open('[name you want the text file.txt]', 'w', encoding='utf-8') as file:
  file.write("[Enter the text you want to be in the file]")


# reading from the file

with open('[existing file.txt]', 'r', encoding='utf-8') as file:
  contents_of_file = file.read()
  print(contents_of_file)
