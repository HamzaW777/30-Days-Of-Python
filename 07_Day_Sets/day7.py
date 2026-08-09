def q1():
    It_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
    A = {19, 22, 24, 20, 25, 26}
    B = {19, 22, 20, 25, 26, 24, 28, 27}
    age = [22, 19, 24, 25, 26, 24, 25, 24]
    print(len(It_companies))
    It_companies.add('Twitter')
    It_companies.update(['LinkedIn', 'Snapchat'])
    It_companies.remove('IBM')
    #lvl2
    AB_union = A.union(B)
    AB_intersection = A.intersection(B)
    print(A.issubset(B))
    print(A.isdisjoint(B))
    A_withB= A.union(B)
    B_withA= B.union(A)
    del A,B
    #lvl3
    age_set = set(age)
    age_list = list(age_set)
    print(len(age_set)==len(age_list))
q1()




