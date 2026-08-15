
import json
with open('file.json', 'r') as file:
    saved_data = json.load(file)
print(saved_data)