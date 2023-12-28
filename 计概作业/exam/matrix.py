n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))
num = -(-n//2)
maxx = 0
for i in range(num):
    summ =0
    summ+= sum(mat[i][i:n-i])
    if i != n-1-i:
        summ+= sum(mat[n-1-i][i:n-i])
    for j in range(i+1,n-1-i):
        summ+= mat[j][i]+mat[j][n-1-i]
    maxx = max(summ,maxx)
print(maxx)