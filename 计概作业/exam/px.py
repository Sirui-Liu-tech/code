'''
2100017810 刘思瑞
'''
import sys
step = [(0,1),(1,0),(-1,0),(0,-1)]
matrix,vis = [],[]
sx,sy = [],[]
ex,ey = 0,0
def dfs(x1,y1,x2,y2):
    global matrix,ex,ey,vis,step
    if (x1,y1) == (ex,ey) or (x2,y2) == (ex,ey):
        print('yes')
        sys.exit()
    for i in step:
        dx , dy = i
        if 0 <= x1+dx < n and 0 <= x2+dx < n and 0 <= y2+dy < n  and 0 <= y1+dy < n and matrix[x1+dx][y1+dy] != 1 and matrix[x2+dx][y2+dy] != 1 and [[x1+dx,y1+dy],[x2+dx,y2+dy]] not in vis:
            vis.append([[x1+dx,y1+dy],[x2+dx,y2+dy]])
            dfs(x1+dx,y1+dy,x2+dx,y2+dy)
    return      
n = int(input())
for i in range(n):
    matrix.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 9:
            ex,ey = i,j
        if matrix[i][j] == 5:
            sx.append(i)
            sy.append(j)
vis.append([[sx[0],sy[0]],[sx[1],sy[1]]])
dfs(sx[0],sy[0],sx[1],sy[1])
print('no')