'''
刘思瑞 2100017810
'''
import re
def find(length , s , round):
    print('Test case #'+str(round))
    i = 0
    for j in range(1,length//2+1):
        if s[j] == s[0]:
            i = j-1
            break
    while i <= length//2:
        j =1
        while True:
            if not re.match('(' + s[:i+1] + '){' + str(j+1)+'}', s):
                break
            j += 1
            print(j*(i+1),j)
        i = j*(i+1)
    print()

round = 1
while True:
    length = int(input())
    if length == 0:
        break
    find(length , input() , round)
    round += 1