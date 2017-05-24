import string

# problem 22
filename = 'names.txt'

# gets a dict of letters to their number pulled from SO
alphabet = {k: v for v, k in enumerate(string.ascii_uppercase, 1)}
names = list()
f = open(filename, "r")

for l in f.readlines():
    for value in l.strip().split(" "):
        names.append(value)
names = sorted(names)


def word_sum(name, position):
    name_sum = 0
    for i in name:
        name_sum += alphabet[i]
    return name_sum * position
all_names = list()
pos = 1
for n in names:
    all_names.append(word_sum(n, pos))
    pos += 1

print sum(all_names)
