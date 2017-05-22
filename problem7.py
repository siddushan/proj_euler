# problem 7

def is_prime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5 # starting point after base cases
    x = 2
    while i * i <= n:
        if n % i == 0:
            return False

        i += x
        x = 6 - x

    return True

count = 0
i = 0
while count != 10001:
    if is_prime(i):
        count += 1
    i += 1
print i
