def q1():
 numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
 negative_zero = [i for i in numbers if  i<=0]
 print(negative_zero)
def q2():
 list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
 flat=[number for row in list_of_lists for number in row]
 print(flat)
def q3():
 tuple=[(i, i**0, i**1, i**2, i**3, i**4, i**5)for i in range(11)]
 print(tuple)
def q4():
 countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
 final_list=[]
 for entry in countries:
  country,city=entry[0]
  final_list=[(country.upper(),country[0:3],city.upper())]  
  print(final_list)
def q5():
 names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
 final=[]
 for entry in names:
  name,prename=entry[0]
  fullname=name+prename
  final=[fullname]
  print(final)
q5()
 


  