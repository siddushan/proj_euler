# problem 16

num = 2 ** 1000
ans = 0
while num > 0:
    ans += num % 10
    num /= 10

print ans
