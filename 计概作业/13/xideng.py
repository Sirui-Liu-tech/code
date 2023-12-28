'''
刘思瑞 2100017810
'''
import copy
li = []
def erupt(l,i):
    global li
    if i == 6:
        li.append(l)
        return
    for j in [0,1]:
        l.append(j)
        erupt(l,i+1)
        l.pop()
    return
X = [[False]*8]
Y = [[False]*8]
for _ in range(5):
    X.append([False] + [bool(x) for x in input().split()] + [False])
    Y.append([[False]*8])    
X.append([[False]*8])
Y.append([[False]*8])
for lii in li:
    A = copy.deepcopy(X)
    B = copy.deepcopy(Y)
    for i in range(1, 7):
        if B[1][i]:
            A[1][i] = not A[1][i]
            A[1][i-1] = not(A[1][i-1])
            A[1][i+1] = not(A[1][i+1])
            A[2][i] = not(A[2][i])
    for i in range(2, 6):
        for j in range(1, 7):
            if A[i-1][j]:
                B[i][j] = True
                A[i][j] = not A[i][j]
                A[i-1][j] = not A[i-1][j]
                A[i+1][j] = not A[i+1][j]
                A[i][j-1] = not A[i][j-1]
                A[i][j+1] = not A[i][j+1]
    if all((not A[5][i] for i in range(1,7))):
        for i in range(1, 6):
            print(" ".join(repr(y) for y in [B[i][1],B[i][2],B[i][3],B[i][4],B[i][5],B[i][6] ]))

