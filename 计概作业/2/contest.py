'''
刘思瑞 2100017810
'''
n , k = map(int, input().split())
contester = list(map(int, input().split()))
omega = contester[k-1]
count = 0
for i in range(n):
    if contester[i] >= max(omega,1):
        count += 1
print(count)