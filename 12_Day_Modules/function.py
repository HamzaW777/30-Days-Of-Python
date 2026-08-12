import random
import string
def random_user_id():
    characters=string.ascii_lowercase+string.digits
    user_id=''
    for i in range(6):
        random_characther=random.choice(characters)
        user_id=user_id+random_characther
    return user_id
#print(random_user_id())
def random_user_id():
    characters=string.ascii_lowercase+string.digits
    x=int(input("how many characters: "))
    y=int(input("how many user_id: "))
    user_id_list=[y]
    for u in range(y):
        user_id=''

        for i in range(x):
        
         random_characther=random.choice(characters)
         user_id=user_id+random_characther
        user_id_list.append(user_id)
        return user_id_list
    
#print(random_user_id())
def rgb_color_gen():
   rgb_color=[]
    
   x=random.randint(0,255)
   rgb_color.append(x)
   y=random.randint(0,255)
   rgb_color.append(y)
   z=random.randint(0,255)
   rgb_color.append(z)
   
   print(rgb_color)
#rgb_color_gen()
import random
import string

def list_of_hexa_colors(number):
    hex_characters = string.digits + 'abcdef'
    hex_list = []

    for i in range(number):
        hex_color = '#'
        for j in range(6):
            random_character = random.choice(hex_characters)
            hex_color = hex_color + random_character
        hex_list.append(hex_color)

    return hex_list

#print(list_of_hexa_colors(3))
def shuffle_list(lst):
    random.shuffle(lst)
    return lst
fruits=['bmw','merc','audi']
#print(shuffle_list(fruits))
def seven_rand():
    array=[]
    for x in range(8):
        number=random.randint(0,9)
        array.append(number)
    return array
print(seven_rand())



      


      
   
