# problem 2
x = 0
x0 = 1
x1 = 2
sum = 2
while x < 4000000:
    if x % 2 == 0:
        sum += x
    x = x0 + x1
    x0 = x1
    x1 = x
print sum
