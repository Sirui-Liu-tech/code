'''
刘思瑞 2100017810
'''
def build(n,k):
    if k > n ** 2:
        print(-1)
        return
    a = []
    m = 0
    for i in range(n):
        a.append([0]*n)
    while True:
        if k == 0:
            for i in a:
                for j in i:
                    print(j,end=' ')
                print('')
            return
        if k >= 2*n - 2*m - 1 :
            for i in range(2*n - 2*m - 1):
                    a[m][i + n - 1 -(2*n - 2*m - 2)] ,a[i + n - 1 -(2*n - 2*m - 2)][m] = 1,1
            k -= 2*n - 2*m - 1 
            m+=1
        else:
            a[m][m] = 1
            k -= 1
            if k%2:
                a[m+1][m+1] = 1
            k = k//2
            for i in range(k):
                a[m][i + m + 1], a[i+m+1][m] = 1,1
            k = 0

n , k = map(int,input().split())
build(n,k)