import operator
import string

with open('input.txt', 'r') as f:
    q = f.readlines()

def get_freq(c, l):
    counts = l.count(c)
    current_list[c] = counts

def decrypt(s, key):
    decrypted = ''
    for i in s:
        if i in string.letters:
            decrypted+= chr(97 + (ord(i)- 97 + key) % 26)
        elif i == '-':
            decrypted+= ' '
    return decrypted

current_list = {}
key_length = 5
ID = 0
part_a_sol = 0
real_rooms = {}
for i in q:
    current_list = {}
    given_hash = ''.join(i.strip().split('-')[-1]).split('[')[1][:-1]
    ID = int(''.join(i.strip().split('-')[-1]).split('[')[0])
    x = ''.join(i.strip().split('-')[:-1])
    y = ' '.join(i.strip().split('-')[:-1])
    
    # count the letters and put them in current_list
    for i in x:
        if i not in current_list.keys():
            get_freq(i, x)

    # thanks to http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
    got_list = sorted(current_list.items(), key=operator.itemgetter(1), reverse=True)

    # alphabetical sorting in case of equal frequency
    right_list = []
    for k in range(len(got_list)-1):
        if got_list[k][1] > got_list[k+1][1]:
            right_list.append(got_list[k][0])
        else:
            if got_list[k][0]< got_list[k+1][0]:
                smaller_index = k
                larger_index = k+1
            else:
                smaller_index = k+1
                larger_index = k
            temp = got_list[larger_index]
            got_list[k] = got_list[smaller_index]
            got_list[k+1] = temp
            right_list.append(got_list[k][0])
            
    calc_hash = ''
    for j in range(key_length):
            calc_hash += right_list[j]

    if calc_hash == given_hash:
        part_a_sol += ID
        real_rooms[y] = ID
        if ''.join('North Pole objects'.lower().split()) in decrypt(y, ID):
            print 'part b solution is', ID

    
print 'part a solution is', part_a_sol


        
    
