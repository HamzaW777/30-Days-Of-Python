def q1():
    lst=[]
    print(lst)
def q2():
    lst=['hamza','soh','sobox','ilass','utsh']
    print(len(lst))
    print(lst[0])
    print(lst[-1])
    print(lst[len(lst)//2])
def q3_25():
    mixed_data_types=['hamza', 20, 5.9, 'single', '123 Main St']
    it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
    print(mixed_data_types)
    print(len(it_companies))
    print(it_companies[0])
    print(it_companies[-1])
    print(it_companies[len(it_companies)//2])
    it_companies.append('Twitter')
    print(it_companies)
    it_companies.insert(3,'Meta')
    print(it_companies)
    print(it_companies[0].upper())
    does_exist = 'Apple' in it_companies
    print(does_exist)
    it_companies.sort()
    print(it_companies)
    first_companies=it_companies[0:3]
    print(first_companies)
    last_companies=it_companies[-4:-1]
    print(last_companies)
    middle_company=it_companies[len(it_companies)//2]
    print(middle_company)
    it_companies.remove(it_companies[0])
    it_companies.remove(it_companies[-1])
    it_companies.remove(it_companies[len(it_companies)//2])
    print(it_companies)
    print(it_companies.clear())
q3_25()
def q26():
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
    full_stack=front_end+back_end
    added_items=['SQL','Python']
    full_stack.extend(added_items)
    print(full_stack)
def q27():
    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
    ages.sort()
    print(ages)
q27()