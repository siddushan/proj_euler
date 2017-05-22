# problem 4

def palindrome(number):
    return str(number) == str(number)[::-1]

init = 0
for i in range(100, 999):
    for j in range(100, 999):
        if palindrome(i * j):
            if i * j > init:
                init = i * j
print init
