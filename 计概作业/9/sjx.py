'''
刘思瑞 2100017810
'''
n = int(input())
matrix = []
maxx = 0
for i in range(n):
    matrix.append(list(map(int,input().split())))
temp = matrix[-1]
for i in range(n-1,0,-1):
    ttemp = []
    for j in range(i):
        ttemp.append(max(matrix[i-1][j]+temp[j],matrix[i-1][j]+temp[j+1]))
    temp = ttemp
print(temp[0])
