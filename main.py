import random

n = int(input("How many dice would you like to roll? "))

m=0

while m < n:
  print(random.randint(1,6))
  m = m + 1