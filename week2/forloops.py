#
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#
for x in "banana":
  print(x)

#
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#5
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#6
for x in range(2, 30, 3):
  print(x) 