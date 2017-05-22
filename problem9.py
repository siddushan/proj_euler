# problem 9

for num in range(1, 1000):
    for d in range(num, 1000 - num):
        i = 1000 - num - d
        if num * num + d * d == i * i:
            print num, d, i
            print num * d * i
