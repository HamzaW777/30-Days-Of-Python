def q1():
    age = int(input('enter your age:'))
    if age >= 18:
        print('you are old enough to drive')
    else:
        print('you need to wait', 18 - age, 'years to drive')
def q2():
    your_age=20
    my_age=int(input('enter your age:'))
    if my_age>your_age:
        print('you are', my_age-your_age, 'years older than me')
    elif my_age<your_age:
        print('you are', your_age-my_age, 'years younger than me')
    else:
        print('we are the same age')
def q3():
    a=int(input('enter a number:'))
    b=int(input('enter another number:'))
    if a>b:
        print(a, 'is greater than', b)
    elif a<b:
        print(a, 'is less than', b)
    else:
        print(a, 'is equal to', b)
def q4():
    score=int(input('your score:'))
    if score>=90 and score<100:
        print('A')
    elif score>=70 and score<90:
        print('B')
    elif score>=60 and score<70:
        print('C')
    elif score>=50 and score<60:
        print('D')
    else:
        print('F')
def q5():
    month=input('enter month:')
    if month=='september' or month=='october' or month=='november':
        print('the season is autumn')
    elif month=='december' or month=='january' or month=='february':
        print('the season is winter')
    elif month=='march' or month=='april' or month=='may':
        print('the season is spring')
    elif month=='june' or month=='july' or month=='august':
        print('the season is summer')
    else:
        print('invalid month')
q5()
