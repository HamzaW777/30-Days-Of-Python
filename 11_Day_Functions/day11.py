def greeting(name):
    message=name + " ,welcome to the world of functions"
    return message
#print(greeting(input("Enter your name: ")))
def add_two_numbers(n,m):
    sum=n+m
    return sum
#print(add_two_numbers(1,2))
def area_of_circle(r):
    area = 3.14 * r * r
    return area
#print(area_of_circle(5))
def add_all_nums(*args):
    print("the type of args is",type(args))
    sum=0
    for num in args:
        sum+=num
    return sum
#print(add_all_nums(1,2,3,4,5))
def convert_celsius_to_fahrenheit(c):
    F = (c * 9/5) + 32
    return F
#print(convert_celsius_to_fahrenheit(37))
def check_season(month):
    if month <3 and month >=1:
     return 'winter'
    elif month <6 and month >=3:
     return 'spring'
    else:
       return'invalid'
#print(check_season(int(input("what month is it"))))
def calculate_slope(x1,x2,y1,y2):
   m= y2-y2/x2-x1
   return m
#print(calculate_slope(2,4,3,6))
import math
def solve_quadratic_eqn(a,b,c):
   d=b*b-4*a*c
   x1=(-b+math.sqrt(d))/(2*a)
   x2=(-b-math.sqrt(d))/(2*a)
   return x1,x2
#print(solve_quadratic_eqn(1,-3,2))
def print_list(n):
   
   for num in n:
      print(num)
  
#(print_list([1,2,4,5]))
def reverse_list(lst):
   reversed_lst=[]
   for x in lst:
      reversed_lst.insert(0,x)
      print(reversed_lst)
#reverse_list(['fofo','bnan','bmw'])
def capitalize_list_items(lst):
    capitalized_lst=[]
    for x in lst:
       capitalized_lst.append(x.capitalize())
    print(capitalized_lst)
#(capitalize_list_items(['fofo','bmw']))
def add_item(item):
   food=['taco','pizza']
   food.append(item)
   return food
#print(add_item('kaka'))
def remove_item(item):
   food=['taco','pizza']
   food.remove(item)
   return food
#print(remove_item('taco'))
def sum_of_numbers(x):
   sum=0
   for numbers in range(x+1):
      sum=sum+numbers
   return sum
#print(sum_of_numbers(5))
def sum_of_even(x):
   sum_even=0
   for number in range(x+1):
    if number%2==0:
      sum_even=sum_even+number
   return sum_even
#print(sum_of_even(6))
#Level 2 
def evens_and_odds(x):
   evens=0
   odds=0
   for i in range(x+1):
      if i%2==0:
         evens+=1
      else:
         odds+=1
   print(f"the numberof odds is{odds}")
   print(f"the numberof evens is{evens}")
#evens_and_odds(100)
def factorial(x):
   result = 1
   for i in range(1,x+1):
      result*=i
   return result 
#print(factorial(5))
def is_empty(v):
   x=len(v)
   if x!=0:
      return False
   else:
      return True
#print(is_empty([]))
def greet(user):
   x=len(user)
   message="hello "+user
   if x==0:
      return 'hello guest!'
   else:
      return message
#print(greet(""))
##level3
def is_prime(x):
   for n in range(2,x-1):
      if n%x==0:
         return False
      else:
         return True
#print(is_prime(7))
def same_type(x):
   m=type(x[0])
   for data in x:
      if type(data) !=m:
         return "not same type"
      else:
         return"same type"
#print(same_type(['banana',2])) 
      