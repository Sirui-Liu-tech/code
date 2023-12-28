'''
刘思瑞 2100017810
'''
def bfs(q,head,tail,steps):
    for k in range(head, tail):
        x, y = q[head]
        head += 1
        if (g[x][y] == 1):
            print(steps)
            return False,False,False,False    
        for z in range(4):
            newx = x + step[z][0]
            newy = y + step[z][1]
            if (check(newx, newy)):
                vis[newx][newy] = 1
                q.append((newx, newy))
                tail += 1
    return q,head,tail,steps+1
def check(x, y):
    if (x < 0 or y < 0 or x >= m or y >= n):
        return False
    if (vis[x][y] or g[x][y] == 2):
        return False
    return True

q = []
step = [[0, 1], [1, 0], [-1, 0], [0, -1]]
vis = [[0] * 52 for _ in range(52)]
g = []
m, n = map(int, input().split())
for i in range(m):
    g.append([int(x) for x in input().split()])
q.append((0, 0))
head = 0
tail = 1
steps = 0
while True:
    q,head,tail,steps = bfs(q,head,tail,steps)
    if not steps:
        break
    if head >= tail:
        print('NO')
        break