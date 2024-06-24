'''
2100017810 刘思瑞
'''
m = []
for i in range(10):
    s = input()
    temp = []
    for j in range(10):
        if s[j] == '-':
            temp.append(0)
        else:
            temp.append(1)
    m.append(temp)
step = [(-1,0),(0,-1),(1,0),(0,1)]
has_vis = set()

def dfs(i,j):
    global m,step,has_vis
    if m[i][j] == 0:
        return
    m[i][j] = 0
    has_vis.add((i,j))
    for _ in step:
        i_,j_ = i+_[0], j+ _[1]
        if i_ < 10 and i_ >=0 and j_ <10 and j_ >= 0 and not((i_,j_) in has_vis) :
            dfs(i_,j_)

count = 0
for i in range(10):
    for j in range(10):
        if m[i][j] == 1:
            dfs(i,j)
            count += 1
print(count)


