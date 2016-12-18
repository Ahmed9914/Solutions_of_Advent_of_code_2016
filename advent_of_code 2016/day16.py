def dragon(s, length):
    x = s + '0' + ''.join([ str(int(not int(i))) for i in s[::-1]])
    
    while len(x) < length:
        x = dragon(x, length)
    return x[:length]
        
def checksum(x):
    y = [x[i:i+2] for i in range(0,len(x),2)]
    
    done = False
    while not done:        
        new = []
        for j in range(len(y)):
            if y[j][0] == y[j][1]:
                y[j] = '1'
            else:
                y[j] = '0'

        y = ''.join(y)
        
        if len(y) % 2 != 0:
            done = True
            
        y = [y[i:i+2] for i in range(0,len(y),2)]
            
    return ''.join(y)

print 'part a solution is', checksum(dragon('01000100010010111', 272))
print 'part b solution is', checksum(dragon('01000100010010111', 35651584))
