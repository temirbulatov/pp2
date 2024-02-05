#task1
class Task1:
    def __init__(self):
        self.userinput = ""

    def getString(self):
        self.userinput = input("Enter a string: ")

    def inUpperCase(self):
        print(self.userinput.upper())

stringt1 = Task1()
stringt1.getString()
stringt1.UpperCase()



#task2 (+3 with rectanlge)
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

x = int(input())
y = int(input())

randomsq = Square(x)
squarea = randomsq.area()
print(f"Area of the square: {squarea}")

randomsh = Shape()
sharea = randomsh.area()
print(f"Area of the shape: {sharea}")

randomrec = Rectangle(x, y)
recarea = randomrec.area()
print(f"Area of the rectangle: {recarea}")



#task4
'''
Point Class
Show() - should represent current location of the point on 2d plane. Coordinates x and y should represent it, can be displayed through the use of 
array of arrays that are limited by 'i' and 'j', then x coordinate location of the point limited by "0 <= x <=i", and y accordingly "0 <= y <=j" .  

Move() - should represent the change of the location of the point along two axises. + or - 1 (or more) but limited by 0 and 'i' (maximum value) for x coordinate; 
+ or - 1 (or more) but limited by 0 and 'j' (maximum value) for y coordinate. Only use of substraction and addition is suitable, not multiplying or division.

Dist() - done through separate calculation of the change in x1 and x2, y1 and y2. Then, trough the use of algebraic formula of Pythagoras Theorem:
Distance = ((x2-x1)^2+(y2-y1)^2)^(1/2). (where x2 and y2 are the highest coordinates among two points, and x1 and x2 vice versa, the smallest ones).
'''



#task5
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        amount = float(input("Amount to be deposited: "))
        self.balance += amount
        

    def withdraw(self):
        amount = float(input("Amount to be withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew: ", amount)
        else:
            print("\n Insufficient balance to withdraw")
    
    def display(self):
        print("\n Net Available Balance of",self.owner, "=",self.balance)
        
o = str(input("Enter the name: "))
b = float(input("Enter the initial capital: "))
a = Account(o, b)

a.deposit()
a.withdraw()
a.display()




#task6

def filter_primes(lst):
    primes = []
    for x in lst:
        if is_prime(x):
            primes.append(x)
    return primes

def is_prime(x):
    cnt = 0
    for i in range(1, x+1):
        if x % i == 0:
            cnt += 1
    return cnt == 2

numbers = list(map(int, input().split()))

prime_numbers = filter_primes(numbers)
print(prime_numbers)