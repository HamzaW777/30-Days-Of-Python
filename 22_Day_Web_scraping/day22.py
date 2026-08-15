import requests
from bs4 import BeautifulSoup
import json

url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

categorys = soup.findAll("h4", attrs={"class": "stat-group-title"})
inss = soup.findAll("ul", attrs={"class": "custom-stat-list"})

data = []

for category, ul in zip(categorys, inss):
    entry = {'category': category.text.strip()}
    items = ul.findAll('li')
    for item in items:
        text = item.text.strip()
        words = text.split()
        value = words[-1]
        label = ' '.join(words[:-1])
        entry[label] = value
    data.append(entry)

with open('/Users/Admin/Desktop/file.json', 'w') as file:
    json.dump(data, file, indent=4)

print('Saved successfully!')
print(data)

