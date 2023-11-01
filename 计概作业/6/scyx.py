'''
刘思瑞 2100017810
'''
def survive(n_,m_):
    global a,n,m
    sum = 0
    if n_ > 0:
        sum += a[n_-1][m_]
        if m_ >0:
            sum += a[n_-1][m_-1]
        try:
            sum += a[n_-1][m_+1]
        except:
            IndexError
    if m_ > 0:
        sum += a[n_][m_-1]
        try:
            sum += a[n_+1][m_-1]
        except:
            IndexError
    try:
        sum += a[n_+1][m_]
    except:
        IndexError
    try:
        sum += a[n_+1][m_+1]
    except:
        IndexError
    try:
        sum += a[n_][m_+1]
    except:
        IndexError
    return sum

a = []
n , m = map(int,input().split())
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        s = survive(i,j)
        out = 0
        if a[i][j] == 0:
            if s == 3:
                out = 1
        else:
            if s ==2 or s == 3:
                out = 1
        print(out,end=' ')
    print('')