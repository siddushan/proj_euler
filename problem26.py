# problem 26

def divide(m, n):
    quotient, c = str(m // n) + ".", 10 * (m % n)
    while c and c < n:
        c *= 10
        quotient += "0"
    digits = " "
    passed = {}
    i = 0
    while True:
        if c in passed:
            cycle = digits[passed[c]:]
            return cycle
        q, r = c // n, c % n
        passed[c] = i
        digits += str(q)
        i += 1
        c = 10 * r

def digits(x):
    dig = [int(x) for i in str(x)]
    return len(dig)

max_num = 0
for i in range(1, 1001):
    v = digits(divide(1, i))
    if v > max_num:
        max_num = v

print max_num
