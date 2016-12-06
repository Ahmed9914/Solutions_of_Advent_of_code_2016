import operator

with open('input.txt', 'r') as input_file:
    k = input_file.read().split('\n')

sol = []
for i in range(len(k[0])):
    x = ''
    for j in range(len(k)):
        x += k[j][i]
    sol.append(x)

part_a_solution = []
part_b_solution = []
for z in sol:
       counts = {}
       for i in z:
           if i not in counts.keys():
               counts[i] = z.count(i)

       part_a_solution.append(sorted(counts.items(), key=operator.itemgetter(1), reverse=True)[0][0])
       part_b_solution.append(sorted(counts.items(), key=operator.itemgetter(1),)[0][0])
print 'part a solution is ', ''.join(part_a_solution)
print 'part b solution is ', ''.join(part_b_solution)
