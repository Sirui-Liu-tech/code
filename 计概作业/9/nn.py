'''
刘思瑞 2100017810
'''
def change(sign):
    if sign == [0,-1]:
        return [-1,0]
    if sign == [-1,0]:
        return [0,1]
    if sign == [0,1]:
        return [1,0]
    if sign == [1,0]:
        return [0,-1]
n = int(input())
m = []
for i in range(n):
    m.append([0]*n)
for i in range(n):
    m[0][i] = i+1
i = n
x = n-1
y = 0
sign = [0,-1]
for j in range(n-1,0,-1):
    for k in range(j):
        i+=1
        x , y = x+sign[0],y-sign[1]
        m[y][x] = i
    sign = change(sign)
    for k in range(j):
        i+=1
        x , y = x+sign[0],y-sign[1]
        m[y][x] = i
    sign = change(sign)
for i in m:
    for j in i:
        print(j,end=' ')
    print('')


