import hashlib, string

# your input here
const = 'reyedfim'

def part_a():
    start = 0
    q = const + str(start)
    hashed = hashlib.md5(q.encode('utf-8')).hexdigest()
    counter = 0
    sol = ''
    while counter < 8:
        hashed = hashlib.md5(q.encode('utf-8')).hexdigest()
        if hashed[:5] != '00000':
            start += 1
            q = const + str(start)
        else:
            sol += str(hashed[5])
            counter += 1
            start += 1
            q = const + str(start)
    return sol

def part_b():
    start = 0
    q = const + str(start)
    hashed = hashlib.md5(q.encode('utf-8')).hexdigest()
    filled_indexes = []
    sol = ['z'] * 8   # any letter after 'f'
    while sol.count('z') > 0:
        hashed = hashlib.md5(q.encode('utf-8')).hexdigest()
        if hashed[:5] != '00000':
            start += 1
            q = const + str(start)
        else:
            if hashed[5] in string.digits:
                if int(hashed[5]) < 8 and int(hashed[5]) not in filled_indexes: 
                    sol[int(hashed[5])] = str(hashed[6])
                    filled_indexes.append(int(hashed[5]))
                    # testing
                    # print hashed[5], hashed[6], sol, sol.count('z')
            start+=1
            q = const + str(start)
    return ''.join(sol)
