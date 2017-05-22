# problem 15
# literally just grid area choose dimension (so for 20x20, 40C20)
from math import factorial

def ncr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

print ncr(40, 20)
