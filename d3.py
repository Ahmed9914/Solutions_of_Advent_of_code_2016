def part_a():
    with open('input.txt', 'r') as input_file:
            q = input_file.readlines()
    count = 0
    sol = 0
    for i in q:
        sides = []
        count+=1
        for j in i.strip().split():
            sides.append(int(j))
        if sides[0] + sides[1] > sides[2] \
           and  sides[1] + sides[2] > sides[0] \
           and sides[0] + sides[2] > sides[1]:
            sol+=1
    return sol

def part_b():
    sol = 0
    count = 0
    with open('input.txt', 'r') as input_file:
            k = input_file.read()
    q = k.replace('\n',' ').split()
    for i in range(0,len(q),9):
        for j in range(3):
            sides = []
            sides = [int(q[i+j]), int(q[i+j+3]), int(q[i+j+6])]
            count += 1
            if sides[0] + sides[1] > sides[2] \
                   and  sides[1] + sides[2] > sides[0] \
                   and sides[0] + sides[2] > sides[1]:
                sol+=1
    return sol
