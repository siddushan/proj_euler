"""
pretty much need to get the corners of every consecutive square

base case:
0th level is just 1
we can get square dimensions with 2n + 1 which means distance of each side is 2n
so at 1st level, we have a 3x3 square (2 spaces between the numbers)
top right (9) is always the area of the square so:
    top right = (2n + 1) ^2
top left is this minus 2n, and same for the other two corners.

so we have
f(n) = (2n + 1)^2 + [(2n + 1)^2 - 2n] + [(2n + 1)^2 - 4n] + [(2n + 1)^2 - 6n]
= [4(2n + 1)^2 - 12n] for the corners

the sum of the diagonals is just this + f(n-1)

now since we're looking for a 1001x1001 spiral:
2n + 1 = 1001
n = 500
we need 500 levels.
"""
base = 1
for n in range(1, 501):
    base += (4*(2*n + 1)**2) - (12 * n)

print(base)
