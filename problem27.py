def q_func(n, a, b):
    return (n ** 2) + (a * n) + b


def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):  # only odd numbers
        if n % i == 0:
            return False

    return True


def count_primes(a, b):
    n = 0
    count = 0
    while is_prime(q_func(n, a, b)):
        count += 1
        n += 1
    return count


"""
base case:
n = 0 implies b must be prime
n = 1 means 1 + a + b must be prime. 
since all primes except 2 are odd, a must be odd.\
"""
n = 0
max_primes = 0
product = 0
for a in range(-999, 1000, 2):
    for b in range(-1000, 1001):
        if (is_prime(b)):
            new_count = count_primes(a, b)
            if new_count > max_primes:
                max_primes = new_count
                product = a * b

print(product, max_primes)

