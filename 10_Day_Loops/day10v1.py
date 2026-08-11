import numbers


def q1():
   for row in range(8):
    line = ''
    for column in range(8):
        line = line + '# '
    print(line)
def q2():
   for a in range(0, 11):
    
    print(a,'x',a,'=',a*a)
   
def q3():
 web_tools = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
 for tool in web_tools:
    print(tool)
def q4():
    for number in range(0,101,2):
       
        print(number)
def q5():
   for number in range(1, 101):
      if number %2!=0:
            print(number)
def q6():
 total = 0
 for number in range(101):
    total = total + number
 print('The sum of all numbers is', total)
def q7():
   total_odds = 0
   total_evens = 0
   for numbers in range(101):
      total_evens = 0
      if numbers %2==0:
         total_evens = total_evens + numbers
         print('The sum of all even numbers is', total_evens)
      else:
            total_odds = total_odds+ numbers
            print('The sum of all odd numbers is', total_odds)
q7()
    