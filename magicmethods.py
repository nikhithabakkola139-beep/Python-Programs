'''
1. Create a class called Product with attributes name and price. Change the + operator so that adding two Product
 objects returns the sum of their prices.

p1 = Product("Keyboard", 1500)
p2 = Product("Mouse", 700)
print(p1 + p2)

Expected Output:
2200print(p1 + p2)'''

class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __add__(self,other):
        return self.price+other.price
p1=Product("Keyboard",1500)
p2=Product("Mouse",700)
print(p1+p2)

'''2. Create a class called BankAccount with an attribute balance. Change the - operator so that 
subtracting one account from another returns the difference between their balances.

account1 = BankAccount(10000)
account2 = BankAccount(3500)
print(account1 - account2)

Expected Output:
6500'''

class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def __sub__(self,other):
        return self.balance-other.balance
account1=BankAccount(10000)
account2=BankAccount(3500)
print(account1-account2)

'''3. Create a class called ShoppingCart with an attribute total. Change the * operator so that multiplying a cart 
by an integer returns the total cost for that many identical carts.

cart = ShoppingCart(2500)
print(cart * 3)

Expected Output:
7500'''

class ShoppingCart:
    def __init__(self,total):
        self.total=total
    def __mul__(self,other):
        return self.total*other

cart=ShoppingCart(2500)
print(cart*3)

'''4. Create a class called Bill with an attribute amount. Change the / operator so that dividing a Bill object 
by a number returns the amount each person must pay.

bill = Bill(1200)
print(bill / 4)

Expected Output:
300.0'''

class Bill:
    def __init__(self,amount):
        self.amount=amount
    def __truediv__(self,other):
        return self.amount/other

bill=Bill(1200)
print(bill/4)

'''5. Create a class called Student with attributes name and marks. Change the > operator so that one student
 is considered greater than another when their marks are higher.

student1 = Student("Anil", 85)
student2 = Student("Ravi", 72)
print(student1 > student2)

Expected Output:
True
'''
class Book:
    def __init__(self,title,isbn):
        self.title=title
        self.isbn=isbn
    def __eq__(self,other):
        return self.isbn==other
book1=Book("python Basics","ISBN101")
book2=Book("Learn Python","ISBN101")
print(book1==book2)

'''6. Create a class called Student with attributes name and marks. Change the > operator so that one student 
is considered greater than another when their marks are higher.

student1 = Student("Anil", 85)
student2 = Student("Ravi", 72)
print(student1 > student2)

Expected Output:
True'''

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __gt__(self,other):
        return self.marks > other.marks

s1=Student("Nik",85)
s2=Student("Manu",72)
print(s1 > s2)

'''7. Create a class called Score with an attribute points. Change the addition behaviour so that an 
integer can be added on the left side of a Score object.

score = Score(80)
print(20 + score)

Expected Output:
100'''

class Score:
    def __init__(self,points):
        self.points=points
    def __radd__(self, other):
        return self.points+other

score=Score(80)
print(20+score)

'''8. Create a class called Inventory with an attribute quantity. Change the += operator so that the supplied
 quantity is added directly to the existing object.

stock = Inventory(50)
stock += 20
print(stock.quantity)

Expected Output:
70'''

class Inventory:
    def __init__(self,quantity):
        self.quantity=quantity
    def __iadd__(self,other):
        self.quantity +=other
        return self

stock=Inventory(50)
stock+=20
print(stock.quantity)

'''9. Create a class called Permission with an attribute containing a set of permission names. Change the
 | operator so that combining two Permission objects returns all unique permissions from both objects.

p1 = Permission({"read", "write"})
p2 = Permission({"write", "delete"})
result = p1 | p2
print(result.permissions)

Expected Output:
{'read', 'write', 'delete'}'''

class Permission:
    def __init__(self,permissions):
        self.permissions=permissions
    def __or__(self,other):
        return Permission(self.permissions | other.permissions)

p1=Permission({"read","write"})
p2=Permission({"write","delete"})
result=p1|p2
print(result.permissions)

'''10. Create a class called Team with attributes name and points. Change the <= operator so that one team 
is considered less than or equal to another when its points are lower than or equal to the other team's points.

team1 = Team("Falcons", 25)
team2 = Team("Tigers", 30)
print(team1 <= team2)

Expected Output:
True'''

class Team:
    def __init__(self,name,points):
        self.name=name
        self.points=points
    def __le__(self, other):
        return self.points<=other.points

team1=Team("Facons",25)
team2=Team("Tigers",30)
print(team1<=team2)
