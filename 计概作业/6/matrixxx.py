'''
刘思瑞 2100017810
'''
def bea(a,b):
    global mat,m,n
    if a != 0 and b!=0 and a != n-1 and b!= m-1:
        if mat[a-1][b-1]:
            if mat[a-1][b] and mat[a][b-1]:
                return True
        if mat[a-1][b+1]:
            if mat[a][b+1] and mat[a-1][b]:
                return True
        if mat[a+1][b+1]:
            if mat[a+1][b] and mat[a][b+1]:
                return True
        if mat[a+1][b-1]:
            if mat[a+1][b] and mat[a][b-1]:
                return True
    elif a == 0:
        if b ==0:
            if mat[a+1][b+1]:
                if mat[a+1][b] and mat[a][b+1]:
                    return True
        elif b==m-1:
            if mat[a+1][b-1]:
                if mat[a+1][b] and mat[a][b-1]:
                    return True
        else:
            if mat[a+1][b+1]:
                if mat[a+1][b] and mat[a][b+1]:
                    return True
            if mat[a+1][b-1]:
                if mat[a+1][b] and mat[a][b-1]:
                    return True
    elif a == n-1:
        if b == 0:
            if mat[a-1][b+1]:
                if mat[a][b+1] and mat[a-1][b]:
                    return True
        elif b == m-1:
            if mat[a-1][b-1]:
                if mat[a-1][b] and mat[a][b-1]:
                    return True
        else:
            if mat[a-1][b-1]:
                if mat[a-1][b] and mat[a][b-1]:
                    return True
            if mat[a-1][b+1]:
                if mat[a][b+1] and mat[a-1][b]:
                    return True
    elif b == 0:
        if mat[a-1][b+1]:
            if mat[a][b+1] and mat[a-1][b]:
                return True
        if mat[a+1][b+1]:
            if mat[a+1][b] and mat[a][b+1]:
                return True
    elif b == m-1:
        if mat[a-1][b-1]:
            if mat[a-1][b] and mat[a][b-1]:
                return True
        if mat[a+1][b-1]:
            if mat[a+1][b] and mat[a][b-1]:
                return True
    return False
    

def sign(a,b):
    global mat
    mat[a][b] = True
    return bea(a,b)

j = 0
n , m , k = map(int,input().split())
mat = []
for i in range(n):
    mat.append([False]*m)
if m != 1 and n !=1 :    
    for i in range(k):
        a , b = map(int,input().split())
        if sign(a-1,b-1):
            j = i+1
            break
print(j)
