# problem 5
flag = True
it = 20
while flag:
    for i in range(1, 20):
        if it % i != 0:
            flag = True
            break
        else:
            flag = False
    it += 20  # since you start at 20 and all need
              # to be multiples of 20, += 20 every time

print it
