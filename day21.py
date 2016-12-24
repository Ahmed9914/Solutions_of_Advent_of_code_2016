from collections import deque

def swap_pos(s, old, new):
    x = [i for i in s]
    if old > new:
        x[new], x[old] = x[old], x[new]
    else:
        x[old], x[new] = x[new], x[old]
    return ''.join(x)

def swap_letter(s, old, new):
    x = [i for i in s]
    if x.index(old) > x.index(new):
        x[x.index(old)], x[x.index(new)] = x[x.index(new)], x[x.index(old)]
    else:
        x[x.index(new)], x[x.index(old)] = x[x.index(old)], x[x.index(new)]
    return ''.join(x)

def rotate(s, steps):
    items = deque(s)
    items.rotate(steps)
    return ''.join(list(items))

def rotate_based(s, letter):
    i = s.index(letter)
    if i >= 4:
        return rotate(s, 1+i+1)
    else:
        return rotate(s, 1+i)

def rotate_based_2(s, letter):
    x = rotate(s, -1)
    i = x.index(letter)
    if i % 2 == 0:
        if i != 0:
            return rotate(s, -i/2 - 1)
        else:
            return rotate(s, -1)
    else:
        if i > 0:
            return rotate(s, -(len(x)/2 + i/2) - 2)
        else:
            return s
            
def reverse(s, from_index, to_index):
    r = s[from_index: to_index+1]    
    return s.replace(s[from_index: to_index+1], r[::-1])

def remove_move(s, from_index, to_index):
    l = [i for i in s]
    t = l[from_index]
    l.remove(t)
    l.insert(to_index, t)
    return ''.join(l)
   
# part a procedure
# Input a password
s = 'abcdefgh'

# Actual input
with open('input.txt', 'r') as f:
    q = f.readlines()

for i in q:
    i = i.strip().split()
    if i[0] == 'swap':
        if i[1] == 'position':
            s = swap_pos(s, int(i[2]), int(i[5]))
        elif i[1] == 'letter':
            s = swap_letter(s, i[2], i[5])
            
    if i[0] == 'rotate':
        if i[1] == 'based':
            s = rotate_based(s, i[-1])
        elif i[1] == 'right':
            s = rotate(s, int(i[2]))
        else:
            s = rotate(s, -int(i[2]))
            
    if i[0] == 'reverse':
        s = reverse(s, int(i[2]), int(i[4]))

    if i[0] == 'move':
        s = remove_move(s, int(i[2]), int(i[5]))

print 'part a solution is', s

# part b procedure
# Input b password
s = 'fbgdceah'
q = q[::-1]

for i in q:
    i = i.strip().split()
    if i[0] == 'swap':
        if i[1] == 'position':
            s = swap_pos(s, int(i[5]), int(i[2]))
        elif i[1] == 'letter':
            s = swap_letter(s, i[5], i[2])
            
    if i[0] == 'rotate':
        if i[1] == 'based':
            s = rotate_based_2(s, i[-1])            
        elif i[1] == 'right':
            s = rotate(s, -int(i[2]))            
        else:
            s = rotate(s, int(i[2]))
            
    if i[0] == 'reverse':
        s = reverse(s, int(i[2]), int(i[4]))


    if i[0] == 'move':
        s = remove_move(s, int(i[5]), int(i[2]))

print 'part b solution is', s
