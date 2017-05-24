from math import sqrt

# problem 21


def sum_divisors(x):
    divisors_list = list()
    y = 1
    while y <= sqrt(x):
        if x % y == 0:
            divisors_list.append(y)
            divisors_list.append(int(x / y))
        y += 1
    divisors_list = sorted(divisors_list)
    divisors_list.pop()
    return sum(divisors_list)

checked = list()  # prevents checking already accounted for pairs
amicable = list()
# can probably make this more efficient by excluding numbers that are prime (since they have no divisors except 1)
# will deal with that later lol
for a in range(2, 10000):
    if a not in checked:
        d_a = sum_divisors(a)
        d_b = sum_divisors(d_a)
        checked.extend([d_a, d_b])
        if a == d_b:
            if d_a != d_b:
                amicable.extend([a, d_a])

print sum(amicable)
