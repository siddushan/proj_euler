__author__ = 'Sidd'

"""
 problem 18 and also problem 67
 just change the txt file input
"""

problem_18 = 'problem18_triangle.txt'
problem_67 = 'p067_triangle.txt'

triangle = list()
with open(problem_18) as input_file: # insert whichever problem you want to here. set to 18 rn
    for line in input_file:
        triangle.append(line.strip().split(' '))
for i in range(len(triangle)):
    for j in range(len(triangle[i])):
        triangle[i][j] = int(triangle[i][j])

while len(triangle) != 1:
    i = 0
    max_values = list()
    while i + 1 < len(triangle):
        max_values.append(max(triangle[len(triangle) - 1][i], triangle[len(triangle) - 1][i + 1]))
        i += 1
    # print max_values
    triangle.pop()
    # print len(triangle)
    updated_row = [x + y for x, y in zip(triangle[len(triangle)-1], max_values)]
    triangle[len(triangle)-1] = updated_row

print triangle
