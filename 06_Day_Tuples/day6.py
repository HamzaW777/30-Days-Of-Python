#exercise 1

def q1():
    empty_tuple = tuple()
    print(empty_tuple)
def q2():
    my_brothers=('fofo','hamza')
    my_sisters=('sara','mona')
    siblings=my_brothers+my_sisters
    print(siblings)
    print(len(siblings))
    parents=('mohamed','sara')
    familly=siblings+parents
    print(familly)
def q3():
    fruits = ('banana', 'orange', 'mango', 'lemon')
    vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
    animal_products = ('Milk', 'Meat', 'Eggs', 'Cheese')
    food_stuff_tp = fruits + vegetables + animal_products
    food_stuff_lt = list(food_stuff_tp)
    
    print(food_stuff_lt[len(food_stuff_lt)//2])
    print(food_stuff_lt[:3])
    print(food_stuff_lt[-3:])
    del food_stuff_tp
def q4():
    nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
    does_exist='Estonia' in nordic_countries
    print(does_exist)
    does_exist2='Iceland' in nordic_countries
    print(does_exist2)
q4()
