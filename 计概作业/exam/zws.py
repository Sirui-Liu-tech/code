from bisect import bisect,bisect_left
n = int(input())
li = []
sa = []
t = 0
d = 0
for i in range(n):
    m= input().split()
    if m[0] == 'add':
        li.insert(bisect(li,[int(m[1]),t]),[int(m[1]),t])
        sa.append(int(m[1]))
        t+=1
    if m[0] == 'del':
        li.pop(bisect_left(li,[sa[d],0]))
        d+=1
    if m[0] == 'query':
        if len(li) %2 != 0:
            print(li[(len(li)-1)//2][0])
        else:
            j = 0.5*(li[(len(li))//2][0]+li[(len(li))//2-1][0])
            if int(j) == j:
                print(int(j))
            else:
                print(j)
