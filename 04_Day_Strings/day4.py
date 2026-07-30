def q1():
    space = " "
    print("Thirty" + space + "Days" + space + "Of" + space + "Python")
def q2():
    space = " "
    print("Coding" + space + "for" + space + "All")
def q3():
    company = "Coding for all"
    print(company)
    print(len(company))
    print(company.upper())
    print(company.lower())
    print(company.capitalize())
    print(company.title())
    print(company.swapcase())
    print(company[7:])
    print(company.find('Coding'))
def q11():
    company = 'Coding for all'
    print(company.replace('Coding','Python'))
def q12():
    Company = 'Python for Everyone'
    print(Company.replace('Everyone','all'))
def q13():
    company="Coding for all"
    print(company.split())
def q14():
    text= 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
    print(text.split(', '))
def q15():
    company="Coding for all"
    print(company[0])
    print(len(company) -1)
    print(company[10])
def q18():
    text = 'Python for everyone'
    word= text.split()
    print(''.join(word[0] for word in word))
def q19():
    text ='coding for all'
    word = text.split()
    print(''.join([word[0] for word in word]))