import requests


online_file = '[Enter link of text file from online]'

request = requests.get(online_file)


with open('[Enter File Name]', 'w', encoding='utf-8') as f:
    f.write(request.text)


