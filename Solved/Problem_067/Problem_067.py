# Project Euler Problem 67

triangle = open('p067_triangle.txt', 'r').readlines()

triangle = [list(map(int, line.split())) for line in triangle]

for row in range(len(triangle)-1, 0, -1):
    for col in range(0, row):
        triangle[row-1][col] += max(triangle[row][col], triangle[row][col+1])

print(triangle[0][0])
