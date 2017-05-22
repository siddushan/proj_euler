# problem 10
from math import sqrt
from itertools import count, islice
def is_prime(number):
    return number > 1 and all(number % i for i in islice(count(2), int(sqrt(number)-1)))

prime_sum = 0
for q in range(2000000):
    if is_prime(q):
        prime_sum += q

print prime_sum
