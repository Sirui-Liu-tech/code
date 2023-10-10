'''
刘思瑞 2100017810
'''
import math
def find(num):
    result = []
    for i in range(1,num+1):
        for j in range(2,i):
            for k in range(j,i):
                rest = i**3 - j**3 -k**3
                if rest >=k**3:
                    for m in range(int(rest**(1/3))+2):
                        if m**3 == rest:
                             result.append([i,j,k,m])
    return result

n = int(input())
re = find(n)
for i in re:
    print('Cube = %d, Triple = (%d,%d,%d)' %(i[0],i[1],i[2],i[3]))
    