sln = set()
for a in range(2, 101):
    for b in range(2, 101):
        num = a ** b
        sln.add(num)

print(len(sln))

