a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#same ouput of true
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15
print(bool(x))
print(bool(y))

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


#always false below
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#functions that may return false or true
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


#exmample bool function with output Yes or No
def myFunction() :
  return True

print(myFunction())

if myFunction():
  print("YES!")
else:
  print("NO!")

#use of isinstance
x = 200
print(isinstance(x, int))
