'''
刘思瑞 2100017810
'''
def find(length , s , round):
    print('Test case #'+str(round))
    i = length//2 +5
    for k in range(1,length//2+1):
        if s[k] == s[0]:
            i = k-1
            break
    while i <= length//2+1:
        j =1
        while True:
            if s[:i+1] != s[j*(i+1):(j+1)*(i+1)]:
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

print()