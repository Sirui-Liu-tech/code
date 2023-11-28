'''
刘思瑞 2100017810
'''
matrix = []
m = 0
for i in range(5):
    matrix.append(list(map(int,input().split())))
for i in range(5):
    inde = matrix[i].index(max(matrix[i]))
    flag = 1
    for j in matrix:
        if j[inde] < max(matrix[i]):
            flag = 0
            break
    if flag == 1:
        print(i+1,matrix[i].index(max(matrix[i]))+1,max(matrix[i]))
        m = 1
if m == 0:
    print('not found')