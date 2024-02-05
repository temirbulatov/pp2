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
