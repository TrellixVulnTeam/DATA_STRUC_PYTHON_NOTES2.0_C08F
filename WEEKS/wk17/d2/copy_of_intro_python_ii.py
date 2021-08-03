# -*- coding: utf-8 -*-
"""Copy of Intro Python II.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14sVd0CenhULFcEnLSSLQr6IOJsDwYmCH

# Intro to Python II
"""

# Slices of lists
[12, 23, 10, 20, 50] 
# sort
numbers = [12, 23, 1, 22]
# print(l[::-1])
# print(dir([]))
# min and max
# print(min(20, 10, 5)) # 5
# print(max(20, 10, 5)) # 20
# list index
# s = "100"
# if "100" in l:
#   print(l.index(s))
# else:
#   print(f"{s} not found")
l2 = []
for number in numbers:
  if number % 2 == 0:
    l2.append(number * 2)
print(l2)

l3 = [number * 2 for number in numbers if number % 2 == 0]
print(l3)

"""# CODE: 6603"""

# Classes and OOP

class Entity:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return f"({self.x}, {self.y})"

class Mob(Entity):
  def __init__(self, x, y):
    super().__init__(x, y)

  def move(self, dir):
    if dir == "n":
      self.y -= 1
    elif dir == "s":
      self.y += 1
    elif dir == "w":
      self.x -= 1
    elif dir == "e":
      self.x += 1 

  

e = Entity(10, 20)
# print(e)

m = Mob(10, 23)
print(m)
m.move("n")
print(m)

"""# CODE: 6603

# Demos

Write a function that retrieves the last n elements from a list.
Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []

Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.
"""

"""
Write a function that retrieves the last n elements from a list.
Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []
Notes:

- Return "invalid" if n exceeds the length of the list.

- Return an empty list if n == 0.

- Return a slice from negative n to the end of the list

"""


def last(a, n):
  if n > len(a):
    return "invalid"
  elif n == 0:
    return []
  return a[-n:]

print(last([1, 2, 3, 4, 5], 1)) # ➞ [5]
print(last([4, 3, 9, 9, 7, 6], 3)) # ➞ [9, 7, 6]
print(last([1, 2, 3, 4, 5], 7)) #  ➞ "invalid"
print(last([1, 2, 3, 4, 5], 0)) # ➞ []

"""Given an integer, write a function that returns "Even" for even integers and
"Odd" for odd integers.
Examples:
- parity(0) -> "Even"
- parity(1) -> "Odd"
- parity(2) -> "Even"

"""

"""
Given an integer, write a function that returns "Even" for even integers and
"Odd" for odd integers.
Examples:
- parity(0) -> "Even"
- parity(1) -> "Odd"
- parity(2) -> "Even"

notes
to get even we can mod by 2
- if the input_int modulo 2 is zero then return even
- otherwise return odd
"""
def parity(input_int):
  if input_int % 2 == 0:
    return "Even"
  else:
    return "Odd"

def parity2(input_int):
  return "Even" if input_int % 2 == 0 else "Odd"

print(parity(0)) #  -> "Even"
print(parity(1)) #  -> "Odd"
print(parity(2)) # -> "Even"

print(parity2(0)) #  -> "Even"
print(parity2(1)) #  -> "Odd"
print(parity2(2)) # -> "Even"