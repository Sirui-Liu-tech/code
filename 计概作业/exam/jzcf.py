n,m1,m2 = map(int,input().split())
a1 = [[0]*n for _ in range(n)]
a2 = [[0]*n for _ in range(n)]
a3 = [[0]*n for _ in range(n)]
for i in range(m1):
    x,y,v = map(int,input().split())
    a1[x][y] = v
for i in range(m2):
    x,y,v = map(int,input().split())
    a2[x][y] = v
for i in range(n):
    for j in range(n):
        for k in range(n):
            a3[i][j] += a1[i][k]*a2[k][j]
for i in a3:
    for j in i:
        print(j,end=' ')
    print()

