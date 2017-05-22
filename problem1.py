# problem 1
this_sum = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        this_sum += i
print this_sum
