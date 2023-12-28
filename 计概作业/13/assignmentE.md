# Assignment #E: 算法基础

Updated 1419 GMT+8 Dec 12, 2023

2023 fall, Complied by ==同学的姓名、院系==



**说明：**

本周作业涉及到枚举、贪心、bfs、矩阵，建议提前开始作业，如果耗时太⻓，直接找答案看。两个题解，经常更新。所以最好从这个链接下载最新的，https://github.com/GMyhf/2020fall-cs101 。

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

3）如果不能在截止前提交作业，请写明原因。



**编程环境**

==（请改为同学的操作系统、编程环境等）==

操作系统：macOS Ventura 13.4.1 (c)

Python编程环境：Spyder IDE 5.2.2, PyCharm 2023.1.4 (Professional Edition)

C/C++编程环境：Mac terminal vi (version 9.0.1424), g++/gcc (Apple clang version 14.0.3, clang-1403.0.22.14.1)



## 1. 题目

如果耗时太⻓，直接看解题思路，或者源码



### 02692: 假币问题

brute force, http://cs101.openjudge.cn/practice/02692



思路：

遍历

##### 代码

```python
'''
刘思瑞 2100017810
'''
for j in range(int(input())):
    L = [[],[],[]]
    flag = 0
    for i in range(3):
        L[i] = input().split()
    for f in 'ABCDEFGHIJKL':
        if all((f in i[0] and i[2]=='up') or (f in i[1] and i[2]=='down') 
               or ( f not in i[0] + i[1] and i[2]=='even') for i in L):
            flag = 'heavy'
            break
        if all((f in i[0] and i[2]=='down') or (f in i[1] and i[2]=='up') 
               or (f not in i[0]+i[1] and i[2]=='even') for i in L):
            flag = 'light'
            break
    print(f +" is the counterfeit coin and it is "+flag+ ".")
```



代码运行截图

![image-20231219214453270](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231219214453270.png)



### 18164: 剪绳子

greedy/huffman, http://cs101.openjudge.cn/practice/18164/



思路：

贪心，但是时间好紧

##### 代码

```python
'''
刘思瑞 2100017810
'''
import bisect
n = int(input())
L = list(map(int,input().split()))
L.sort()
sum = 0
for i in range(n-1):
    sum += L[0] + L[1]
    bisect.insort(L,L[0]+L[1])
    L = L[2:]
print(sum)
```



代码运行截图

![image-20231219215825115](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231219215825115.png)

### 01328: Radar Installation

greedy, http://cs101.openjudge.cn/practice/01328/



思路：

按岛屿 x 坐标排序，贪心遍历岛屿，每次选择最优的雷达安装位置以最小化雷达数量，同时根据当前岛屿更新雷达的覆盖范围

##### 代码

```python
import math

def minimal_radar_installations(n, d, islands):
    islands.sort(key=lambda x: x[0])
    radar_count = 0
    current_position = -math.inf
    for island in islands:
        x, y = island
        if y > d:
            return -1  
        if x - y > current_position:
            current_position = x + y
            radar_count += 1
        elif x + y >= current_position:
            current_position = x + y
    return radar_count

case_number = 0
while True:
    n, d = map(int, input().split())
    if n == 0 and d == 0:
        break

    case_number += 1
    islands = [list(map(int, input().split())) for _ in range(n)]
    result = minimal_radar_installations(n, d, islands)

    print(f"Case {case_number}: {result}")
    input()
```



代码运行截图

![image-20231219232819230](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231219232819230.png)



### 19930: 寻宝

bfs, http://cs101.openjudge.cn/practice/19930



思路：

bfs

##### 代码

```python
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
```



代码运行截图 

![image-20231219221621542](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231219221621542.png)





### 1163B2. Cat Party (Hard Edition)

https://codeforces.com/contest/1163/problem/B2
好题。通过维护双层（三层？）数据结构可以O(n)。

确实好题，而且感觉难度适合作业没有复杂的东西。多维护了几个数就做到O(n)了。



思路：



##### 代码

```python
'''
刘思瑞 2100017810
'''
n=int(input())
l=list(map(int,input().split()))
a,b=[0]*(10**6),[0]*(10**6)
ans=1
j=1
for i in range(0,n):
    a[l[i]]+=1
    b[a[l[i]]]+=1
    if a[l[i]]*b[a[l[i]]]==j and j!=n:
        ans=j+1
    elif a[l[i]]*b[a[l[i]]]==j-1:
        ans=j
    j+=1
print(ans)
```



代码运行截图 ==不知道为什么这个一直在队列里面没有跑==

![image-20231219232005279](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231219232005279.png)





### 02811: 熄灯问题

brute force, http://cs101.openjudge.cn/practice/02811



思路：

遍历第一层

##### 代码

```python
'''
刘思瑞 2100017810
'''
import copy
li = []
def erupt(l,i):
    global li
    if i == 6:
        li.append(l)
        return
    for j in [0,1]:
        l.append(j)
        erupt(l,i+1)
        l.pop()
    return
X = [[False]*8]
Y = [[False]*8]
for _ in range(5):
    X.append([False] + [bool(x) for x in input().split()] + [False])
    Y.append([[False]*8])    
X.append([[False]*8])
Y.append([[False]*8])
for lii in li:
    A = copy.deepcopy(X)
    B = copy.deepcopy(Y)
    for i in range(1, 7):
        if B[1][i]:
            A[1][i] = not A[1][i]
            A[1][i-1] = not(A[1][i-1])
            A[1][i+1] = not(A[1][i+1])
            A[2][i] = not(A[2][i])
    for i in range(2, 6):
        for j in range(1, 7):
            if A[i-1][j]:
                B[i][j] = True
                A[i][j] = not A[i][j]
                A[i-1][j] = not A[i-1][j]
                A[i+1][j] = not A[i+1][j]
                A[i][j-1] = not A[i][j-1]
                A[i][j+1] = not A[i][j+1]
    if all((not A[5][i] for i in range(1,7))):
        for i in range(1, 6):
            print(" ".join(repr(y) for y in [B[i][1],B[i][2],B[i][3],B[i][4],B[i][5],B[i][6] ]))
```



代码运行截图

![image-20231219231822414](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231219231822414.png)





### 02802: 小游戏

dfs, bfs, http://cs101.openjudge.cn/practice/02802/ 



思路：

实在想不明白自己的bug在哪里，先交个标答我再慢慢想（（（

##### 代码

```python
import sys
sys.setrecursionlimit(1000000)
d=[(0,-1),(0,1),(-1,0),(1,0)]
H,L,ha,la,hb,lb,MIN=0,0,0,0,0,0,0
b=0
def dfs(h,l,dire,step):
    global H,L,hb,lb,MIN,b
    if h==hb and l==lb:
        if step<MIN:
            MIN=step
        return
    if step>=MIN:
        return
    for i in d:
        hh,ll=h+i[0],l+i[1]
        if hh>=0 and hh<=H+1 and ll>=0 and ll<=L+1 and b[hh][ll]==' ':
            b[hh][ll]='X'
            if dire!=i:
                dfs(hh,ll,i,step+1)
            else:
                dfs(hh,ll,i,step)
            b[hh][ll]=' '
            
k1=0
while True:
    k1+=1
    L,H=map(int,input().split())
    if L==0:
        break
    print("Board #{}:".format(k1))
    b=[[' ']*(L+2)]
    for _ in range(H):
        b.append([' ']+list(input())+[' '])
    b.append([' ']*(L+2))
    k2=0
    while True:
        k2+=1
        la,ha,lb,hb=map(int,input().split())
        MIN=float('inf')
        if la==0:
            break
        b[hb][lb]=' '
        dfs(ha,la,(0,0),0)
        b[hb][lb]='X'
        if MIN==float('inf'):
            print("Pair {}: impossible.".format(k2))
        else:
            print("Pair {}: {} segments.".format(k2,MIN))
    print()
```



代码运行截图

![image-20231219233323621](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231219233323621.png)



## 2. 学习总结和收获

主要复习了搜索算法和递归算法，还是有思路但是找不到bug的问题





