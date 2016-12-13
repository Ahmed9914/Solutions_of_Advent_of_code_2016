from pprint import PrettyPrinter
import numpy as np

mat = [['.' for i in range(50)] for j in range(6)]
with open('input.txt', 'r') as f:
    q = f.readlines()

mat = np.array(mat)
a, b = 0, 0
sol_a = 0
for i in q:
    i = i.split()
    if i[0] == 'rect':
        cols = int(i[1].split('x')[0])
        rows = int(i[1].split('x')[1])
        for y in range(rows):
            for x in range(cols):
                mat[y][x] = '#' 
    elif i[0] == 'rotate':
        if i[1] == 'column':
            col_no = int(i[2].split('=')[1])
            shift = int(i[4])
            mat[:,col_no] = np.roll(mat[: , col_no], shift)
        elif i[1] == 'row':
            row_no = int(i[2].split('=')[1])
            shift = int(i[4])
            mat[row_no] = np.roll(mat[row_no], shift)

mat = mat.tolist()
for i in mat:
    sol_a += i.count('#')
print 'part a solution', sol_a
print 'part b solution (read it yourself) :)'
for j in range(0,50,5):
    for i in mat:
        print ''.join(i[j:j+5])
    print '-','-'
