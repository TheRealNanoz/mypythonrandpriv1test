from random import *

def random_integer(min, max):
  x = randint(min, max)
  print(f"your random number between {min} and {max} is: {x}")

min = int(input("Enter min: "))
max = int(input("Enter max: "))
random_integer(min, max)
