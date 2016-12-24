current_dir = "up"
current_pos = [0, 0]
steps = 0
directions = {"up": 1, "down": -1, \
              "left": -1, "right": 1}
xs, ys=[], []

with open('input.txt', 'r') as f:
    l = f.read().split(', ')

def walk(key, s):
    if key == "up" or key == "down":
        current_pos[1] += directions[key] * s
    else:
        current_pos[0] += directions[key] * s
 
for i in range(len(l)):
    if l[i][0] == 'R':
        if current_dir == "up":
            current_dir = "right"
        elif current_dir == "right":
            current_dir = "down"
        elif current_dir == "down":
            current_dir = "left"
        elif current_dir == "left":
            current_dir = "up"
            
    elif l[i][0] == 'L':
        if current_dir == "up":
            current_dir = "left"
        elif current_dir == "right":
            current_dir = "up"
        elif current_dir == "down":
            current_dir = "right"
        elif current_dir == "left":
            current_dir = "down"
    walk(current_dir, int(l[i][1:]))
    xs.append(current_pos[0])
    ys.append(current_pos[1])
    #print 'walked to ',current_dir, int(l[i][1:]),current_pos,l[i]

    
print 'solution of part a is: ',abs(current_pos[0])+abs(current_pos[1])

import matplotlib.pyplot as plt
plt.plot(xs, ys)
plt.show()            
print 'solution of part b can be got from the plot'
