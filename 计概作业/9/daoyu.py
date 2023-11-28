'''
刘思瑞 2100017810
'''
n ,m =map(int,input().split())
matrix = [[0]*(m+2)]
for i in range(n):
    matrix.append([0]+list(map(int,input().split()))+[0])
matrix.append([0]*(m+2))
c = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if matrix[i][j]:
            c += 4-(matrix[i+1][j]+matrix[i][j+1]+matrix[i][j-1]+matrix[i-1][j])
print(c)
