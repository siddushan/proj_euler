# problem 15
# literally just grid area choose dimension (so for 20x20, 40C20)

def ncr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

print ncr(40, 20)
