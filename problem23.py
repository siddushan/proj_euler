from math import sqrt
# problem 23


def sum_divisors(x):
    divisors_list = list()
    y = 1
    while y <= sqrt(x):
        if x % y == 0:
            divisors_list.append(y)
            if y != (x / y):
                divisors_list.append(x / y)
        y += 1
    divisors_list.sort()
    divisors_list.pop()
    return sum(divisors_list)


def binary_search(seq, t):
    flag = False
    bottom = 0
    top = len(seq) - 1
    while bottom <= top and not flag:
        middle = (bottom + top) / 2
        if seq[middle] == t:
            flag = True
        elif seq[middle] < t:
            bottom = middle + 1
        else:
            top = middle - 1
    return flag

abundant_numbers = list()
abundant_numbers.append(12)  # initial from problem

for i in range(13, 28123):
    s = sum_divisors(i)
    if s > i:
        abundant_numbers.append(i)

check_list = set()

for i in abundant_numbers:
    for j in abundant_numbers:
        s = i + j
        if s <= 28123:  # only check when sum < 28123 and prevent duplicates
            check_list.add(s)
        else:
            break
sum_ans = 0
check_list = sorted(check_list)
for i in range(28123):
    if not binary_search(check_list, i):
        sum_ans += i

print 'sum', sum_ans
