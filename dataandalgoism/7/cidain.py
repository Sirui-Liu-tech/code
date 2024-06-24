'''
2100017810 刘思瑞
'''
from collections import deque
M,N = map(int,input().split())
l = list(map(int,input().split()))
m = deque()
count = 0
for i in l:
    if i in m:
        continue
    if len(m) == M:
        m.popleft()
    m.append(i)
    count +=1
print(count)