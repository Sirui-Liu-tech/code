'''
刘思瑞 2100017810
'''
import heapq
m,n,p = map(int,input().split())
F = []
for i in range(m):
    F.append(list(input().split()))
step = [(0,1),(0,-1),(1,0),(-1,0)]
def bfs(s0,s1,o0,o1):
    global step,F
    has_vis = set()
    has_vis.add((s0,s1))
    heap = []
    heapq.heappush(heap,(0,s0,s1))
    ans = []
    while heap:
        ene,x,y = heapq.heappop(heap)
        if x == o0 and y==o1:
            ans.append(ene)
            continue 
        for i in step:
            d0,d1 = i
            x1,y1 = x + d0,y+d1
            if 0 <= x1 < m and 0 <= y1 < n and F[x1][y1] != '#' and (x1, y1) not in has_vis:
                heapq.heappush(heap,(ene+abs(int(F[x1][y1])-int(F[x][y])),x1,y1))
                has_vis.add((x1,y1))
    return ans
for i in range(p):
    s0,s1,o0,o1 = map(int,input().split())
    if F[s0][s1] == '#' or F[o0][o1] == '#':
        print('NO')
        continue
    ans = bfs(s0,s1,o0,o1)
    if ans:
        print(min(ans))
    else:
        print('NO')