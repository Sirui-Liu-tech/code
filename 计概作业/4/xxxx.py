'''
刘思瑞 2100017810
'''
def calcu(le,x,array):
    nonzero = []
    for i in range(le):
        array[i] %= x
        if array[i] != 0:
            nonzero.append(i)
    sum = -1
    if len(nonzero) ==0:
        return sum
    if len(nonzero) ==1:
        return le
    sum = nonzero[0] +1
    nsum = 0
    for j in range(0,len(nonzero)):
        nsum += array[nonzero[j]]
        if nsum % x != 0:
            if j+1 < len(nonzero):
                if nonzero[j+1] >sum:
                    sum = nonzero[j+1]
            else:
                return le
    return sum


n = int(input())
for i in range(n):
    le , x = map(int,input().split())
    array = list(map(int,input().split()))
    print(max(calcu(le,x,array),calcu(le,x,array[::-1])))