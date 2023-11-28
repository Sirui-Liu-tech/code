'''
刘思瑞 2100017810
'''
def find(n):
    m = [1,2]
    for i in range(2,n):
        m.append((2*m[i-1]+m[i-2])%32767)
    return m

li = []
num = int(input())
for i in range(num):
    li.append(int(input()))
n = max(li)
m = find(n)
for i in li:
    print(m[i-1])

