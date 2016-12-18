# Actual input
input_act = '...^^^^^..^...^...^^^^^^...^.^^^.^.^.^^.^^^.....^.^^^...^^^^^^.....^.^^...^^^^^...^.^^^.^^......^^^^'

def solution(my_input, no_of_floors):
    floors = [my_input]
    for i in range(no_of_floors-1):
        current_floor = floors[i]
        next_floor = ['0'] * len(current_floor)
        for c in range(len(current_floor)):
            if c==0:
                if (current_floor[c] == '.' and current_floor[c+1] == '^') or \
                   (current_floor[c] == '^' and current_floor[c+1] == '^'):
                    next_floor[0] = '^'
                else:
                    next_floor[0] = '.'
            elif c == len(current_floor)-1:
                if (current_floor[c] == '.' and current_floor[c-1] == '^') or \
                   (current_floor[c] == '^' and current_floor[c-1] == '^'):
                    next_floor[len(current_floor)-1] = '^'
                else:
                    next_floor[len(current_floor)-1] = '.'
            else:
                #Its left and center tiles are traps, but its right tile is not
                #Its center and right tiles are traps, but its left tile is not
                #Only its left tile is a trap
                #Only its right tile is a trap
                if (current_floor[c] == '^' and current_floor[c+1] == '.' and current_floor[c-1] == '^') or \
                   (current_floor[c] == '^' and current_floor[c+1] == '^' and current_floor[c-1] == '.') or \
                   (current_floor[c] == '.' and current_floor[c+1] == '.' and current_floor[c-1] == '^') or \
                   (current_floor[c] == '.' and current_floor[c+1] == '^' and current_floor[c-1] == '.'):  
                    next_floor[c] = '^'
                else:
                    next_floor[c] = '.'
        floors.append(''.join(next_floor))
    sol = 0
    for i in floors:
        sol += i.count('.')
    return sol

print 'part a solution is', solution(input_act, 40)
print 'part b solution is', solution(input_act, 400000)                
            

