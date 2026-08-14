with open("/Users/Admin/Desktop/Python30/30-Days-Of-Python/19_Day_File_handling/file.txt",'w') as file:
 content=file.write('claude is the best ai agent')

#print(content)
with open("/Users/Admin/Desktop/Python30/30-Days-Of-Python/19_Day_File_handling/file.txt",'r') as file:
 content=file.read()

#print(content)


import json

person = {
    'name': 'hamza',
    'age': '20',
    'lan': 'darija'
}

with open("/Users/Admin/Desktop/file.json", 'w') as file:
    json.dump(person, file)


print('File created successfully')

   



 
