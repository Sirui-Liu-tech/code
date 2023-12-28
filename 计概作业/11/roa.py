'''
刘思瑞 2100017810
'''
num = int(input())
for k in range(num):
    m = []
    sum = 0
    n = int(input())
    for i in range(n):
        s = input()
        temp = []
        for j in range(n):
            temp.append(s[j])
        m.append(temp)
    for i in range(n//2):
        for j in range(n//2):
            t = max(m[i][j],m[n-1-i][n-1-j],m[j][n-1-i],m[n-1-j][i])
            sum += 4*ord(t) - ord(m[i][j])-ord(m[n-1-i][n-1-j])-ord(m[j][n-1-i]) - ord(m[n-1-j][i])
    print(sum)
