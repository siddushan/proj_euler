from math import factorial
# problem 20

x = factorial(100)

digits = [int(x) for x in str(x)]

print sum(digits)
