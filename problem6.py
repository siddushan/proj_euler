# problem 6

naturals = list()
for i in range(1, 101):
    naturals.append(i)

square_of_sum = sum(naturals) ** 2
squares = [x**2 for x in naturals]
sum_of_squares = sum(squares)
print square_of_sum - sum_of_squares
