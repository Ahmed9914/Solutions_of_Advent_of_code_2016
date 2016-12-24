def part_a():
    keypad = [[1, 2, 3],\
              [4, 5, 6],\
              [7, 8, 9]]
    x=1  # 3>x>=0
    y=1  # 3>x>=0
    sol = ""
    f = open('input.txt', 'r')
    l = f.read().split()
    f.close()
    for i in l:
        for c in i:
            if c=='U' and x>0:
                x-=1
            elif c=='D' and x<2:
                x+=1
            elif c=='R' and y<2:
                y+=1
            elif c=='L' and y>0:
                y-=1
        sol+=str(keypad[x][y])
    return sol
#***********************************************************#
def part_b():
    keypad = [     [1], \
                [2, 3, 4],\
             [5, 6, 7, 8, 9],\
              ['A','B','C'],\
                  ['D']\
             ]
    x=2
    y=0
    sol = ""
    f = open('input.txt', 'r')
    l = f.read().split()
    f.close()
    for i in l:
        for c in i:
            if c=='U':
                if x==1 and y==1:
                    x=0
                    y=0
                elif x==2 and y>0 and y<3:
                    x-=1
                    y-=1
                elif x==3 and y>=0 and y<3:
                    x-=1
                    y+=1
                elif x==4 and y==0:
                    x-=1
                    y=1
            elif c=='D':
                if x==0 and y==0:
                    x=1
                    y=1
                elif x==1 and y>=0 and y<3:
                    x+=1
                    y+=1
                elif x==2 and y>0 and y<4:
                    x+=1
                    y-=1
                elif x==3 and y==1:
                    x=4
                    y=0
            elif c=='R':
                if (x==1 and y<2 and y>=0)\
                   or (x==2 and y<4 and y>=0)\
                   or (x==3 and y<2 and y>=0):
                    y+=1
            elif c=='L':
                if (x==1 or x==2 or x==3) and y>0:
                    y-=1
        sol+=str(keypad[x][y])
    return sol
        
