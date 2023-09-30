"""
刘思瑞 2100017810
"""
L , M =  map(int, input().split())
tree = [1]*(L+1)
for i in range(M):
    origin , determination = map(int, input().split())
    for j in range(origin , determination+1):
        tree[j] = 0
n = 0
for i in tree:
    n += i
print(n)