# problem 14
list_zeroes = [0] * 1000000

def collatz(n):
    count = 1
    x = n
    while n != 1:
        if n % 2 == 0:
            n /= 2
            count += 1
        else:
            n = 3 * n + 1
            count += 1
        if n < 1000000:
            if list_zeroes[n] != 0:
                list_zeroes[x] = count + list_zeroes[n]
                return count + list_zeroes[n]
    list_zeroes[x] = count

    return count
max_len = 0
val = 0
for i in range(1, 1000000):
   #  print i
    col_len = collatz(i)
    if col_len > max_len:
        max_len = col_len
        val = i

print val
