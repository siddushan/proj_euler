# problem 25


def get_num_digits(x):
    digits = [x for i in str(x)]
    return len(digits)

f1_init = 1
f2_init = 1
i = get_num_digits(f1_init)
count = 2
while i < 1000:
    next_num = f1_init + f2_init
    count += 1
    i = get_num_digits(next_num)
    f1_init = f2_init
    f2_init = next_num

print count
