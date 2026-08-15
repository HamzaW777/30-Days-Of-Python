class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person('hamza',20)
p2=person('ffofo',21)    
#print(p1.name)

    
class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return self.sum() / self.count()
    def median(self,data):
        sorted_data=sorted(self,data)
        n=len(sorted_data)
        mid=n//2
        if n%2==0:
            return (sorted_data[mid-2]+sorted_data[mid])
        else:
            return sorted_data[mid]
class PersonAcc:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.income = []
        self.expenses = []

    def add_income(self, amount, desc):
        self.income.append({'amount': amount, 'description': desc})

    def add_expenses(self, amount, desc):
        self.expenses.append({'amount': amount, 'description': desc})

    def total_income(self):
        total = 0
        for entry in self.income:
            total = total + entry['amount']
        return total

    def total_expenses(self):
        total = 0
        for entry in self.expenses:
            total = total + entry['amount']
        return total

    def account_balance(self):
        return self.total_income() - self.total_expenses()

    def account_info(self):
        return f'{self.firstname} {self.lastname}'
account = PersonAcc('Hamza', 'W')
account.add_income(500, 'salary')
account.add_expenses(100, 'groceries')
print(account.account_info())       # 
print(account.total_income())        
print(account.total_expenses())      
print(account.account_balance())     
class Library:
    def __init__(book, title):
        book.title = title
        book.books = []

    def add_book(book, title, author):
        book.books.append({'title': title, 'author': author, 'available': True})

    def total_book(book):
        return len(book.books)

    def available_books(book):
        available = []
        for x in book.books:
            if x['available'] == True:
                available.append(x['title'])
        return available

    def borrow_book(book, title):
        for y in book.books:
            if y['title'] == title:
                y['available'] = False

    def return_book(book, title):
        for x in book.books:
            if x['title'] == title:
                x['available'] = True

    def library_info(book):
        return f'Central library has {len(book.books)} books.'
lib = Library('Central Library')
lib.add_book('1984', 'George Orwell')
lib.add_book('Dune', 'Frank Herbert')

print(lib.library_info())       
print(lib.available_books())    

lib.borrow_book('1984')
print(lib.available_books())   

lib.return_book('1984')
print(lib.available_books())                
                    
         