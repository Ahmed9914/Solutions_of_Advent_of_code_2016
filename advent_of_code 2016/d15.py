d1, d2, d3, d4, d5, d6, t = 10, 15, 17, 1, 0, 1, 0
while True:
    d1, d2, d3, d4, d5, d6 = d1%13, d2%17, d3%19, d4%7, d5%5, d6%3
    if d1 == 12 and d2 == 15 and d3 == 16 and d4 == 3 and d5 == 0 and d6 == 0:
        break
    d1+=1
    d2+=1
    d3+=1
    d4+=1
    d5+=1
    d6+=1
    t+=1
    
print 'part a solution is', t    

d1, d2, d3, d4, d5, d6, d7, t = 10, 15, 17, 1, 0, 1, 0, 0
while True:
    d1, d2, d3, d4, d5, d6, d7 = d1%13, d2%17, d3%19, d4%7, d5%5, d6%3, d7%11
    if d1 == 12 and d2 == 15 and d3 == 16 and d4 == 3 and d5 == 0 and d6 == 0 and d7 == 4:
        break
    d1+=1
    d2+=1
    d3+=1
    d4+=1
    d5+=1
    d6+=1
    d7+=1
    t+=1
    
print 'part b solution is', t   
