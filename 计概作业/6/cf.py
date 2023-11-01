'''
刘思瑞 2100017810
'''
def vecx(a,b):
    global n
    sum = 0
    for i in range(n):
        sum += a[i]*b[i]
    return sum
        
n , m1 , m2 = map(int,input().split())
a = []
b = []
a_arr = []
b_arr = []
li = [0]*n
r , c , num = map(int,input().split())
a.append(r)
li[c] = num
for i in range(m1-1):
    r , c , num = map(int,input().split())
    if r not in a:
        a.append(r)
        a_arr.append(li)
        li = [0]*n
    li[c] = num
a_arr.append(li)
r , c , num = map(int,input().split())
b.append(c)
li = [0]*n
li[r] = num
b_arr.append(li)
for i in range(m2-1):
    r , c , num = map(int,input().split())
    if c not in b:
        b.append(c)
        b_arr.append([0]*n)
        b_arr[-1][r] = num
    else:
        b_arr[b.index(c)][r] = num
b_arr.append(li)
for i in range(len(b)-1):
    for j in range(len(b)-1-i):
        if b[j] > b[j+1]:
            b[j] , b[j+1] , b_arr[j] , b_arr[j+1] = b[j+1] , b[j] , b_arr[j+1] , b_arr[j]
for i in a:
    for j in b:
        m = vecx(a_arr[a.index(i)],b_arr[b.index(j)])
        if m:
            print(i,j,m)