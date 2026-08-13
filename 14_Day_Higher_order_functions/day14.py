

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#for x in countries:
   # print(x)
#for y in names :
    #print(y)
#for z in numbers:
 #   print(z)
def upper_case(text):
    return text.upper() 
upper_country=list(map(upper_case,countries))
#print(upper_country)
def square(x):
    return x*x
squared=list(map(square,numbers))
#print(squared)
def upper_case(text):
    return text.upper() 
upper_names=list(map(upper_case,names))
#print(upper_names)
def check(x):
        if 'land'in x:
            return True
        else :
            return False
new_cou=(filter(check,countries))
#print(list(new_cou))
def check2(x):
        nc=len(x)
        if nc<=6:
            return True
        else :
            return False
new_cou=(filter(check2,countries))
#print(list(new_cou))
def check3(x):
        entry=countries[0]
        if  x[0]=='E':
            return True
        else :
            return False
new_cou=(filter(check3,countries))
print(list(new_cou))



