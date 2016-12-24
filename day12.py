# Actual input
with open('input.txt', 'r') as f:
    q = f.readlines()

# Test value
##q = ['cpy 41 a' , 'inc a' ,'inc a','dec a','jnz a 2','dec a']
def instructions(a, b, c):
    i = 0
    while i < len(q):
        if q[i].split()[0] == 'cpy':
            exec(q[i].split()[2]+'='+q[i].split()[1])
            i += 1
        elif q[i].split()[0] == 'inc':
            exec(q[i].split()[1]+'+=1')
            i += 1
        elif q[i].split()[0] == 'dec':
            exec(q[i].split()[1]+'-=1')
            i += 1
        elif q[i].split()[0] == 'jnz':
            if eval(q[i].split()[1]) != 0:
                i += int(q[i].split()[2])
            else:
                i += 1
    return a

print 'solution of part a', instructions(0, 0, 0)
print 'solution of part b', instructions(0, 0, 1)
