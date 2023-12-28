# Assignment #F: 十全十美

Updated 1305 GMT+8 Dec 19, 2023

2023 fall, Complied by ==同学的姓名、院系==



**说明：**

本周作业对零基础同学偏难，如果耗时太⻓，直接找答案看。两个题解，经常更新。所以最好从这个链接下载最新的，https://github.com/GMyhf/2020fall-cs101 。

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



### 18155: 组合乘积

dfs, brute force, http://cs101.openjudge.cn/practice/18155



思路：

要特别注意目标是1的情况

##### 代码

```python
'''
刘思瑞 2100017810
'''
import sys
N = int(input())
S = list(map(int,input().split()))
num  = len(S)
def dfs(N,S,i):
    if N == 1:
        print('YES')
        sys.exit()
    for j in range(i+1,num):
        if N%S[j] ==0:
            dfs(N//S[j],S,j)
    return
if N ==1:
    if 1 in S:
        print('YES')
    else:
        print('NO')
else:
    dfs(N,S,-1)
    print('NO')
```



代码运行截图

![image-20231226045557311](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231226045557311.png)



### 20106: 走山路

bfs, http://cs101.openjudge.cn/practice/20106/



思路：

bfs

##### 代码

```python
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
    has_vis.add((s0,s1,-1))
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
            if 0 <= x1 < m and 0 <= y1 < n and F[x1][y1] != '#' and (x1, y1,i) not in has_vis:
                heapq.heappush(heap,(ene+abs(int(F[x1][y1])-int(F[x][y])),x1,y1))
                has_vis.add((x1,y1,i))
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
```



代码运行截图 

![image-20231226060646601](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231226060646601.png)



### 27314: 一键换词

implementation, string, http://cs101.openjudge.cn/practice/27314/



思路：

尤其注意是每句话首字母大写

##### 代码

```python
'''
刘思瑞 2100017810
'''
s = list(input().split())
w,dw = input().split()
w = w.lower()
dw = dw.lower()
sw =[w,w+',',w+'.',':'+w]
sdw =[dw,dw+',',dw+'.',':'+dw]
for i in range(len(s)):
    s[i] =s[i].lower()
    if s[i] in sw:
        s[i] = sdw[sw.index(s[i])]
s[0] = s[0][:1].upper() + s[0][1:]
for i in range(len(s)-1):
    if '.' in s[i]:
        s[i+1] = s[i+1][:1].upper() + s[i+1][1:]
for i in s:
    print(i,end=' ')
```



代码运行截图

![image-20231226062345691](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231226062345691.png)





### 19961: 最大点数(外太空2048)

matrices, http://cs101.openjudge.cn/practice/19961/



思路：

实在没懂题目，直接看题解了

##### 代码

```python
import copy
import sys
sys.setrecursionlimit(1<<30)
m,n,p=map(int,input().split())
matrix=[]
for _ in range(m):
    matrix.append(list(map(int,input().split())))

def add(lst):
    for i in range(len(lst)-1):
        if lst[i]!=0:
            for j in range(i+1,len(lst)):
                if lst[i]==lst[j]:
                    lst[i],lst[j]=0,2*lst[i]
                    break
                elif lst[j]==0:
                    pass
                else:
                    break
    ans=[]
    count=0
    for i in lst:
        if i!=0:
            ans.append(i)
            count+=1
    return [0]*(len(lst)-count)+ans
            
        
def move(matrix,dirc):
    new=copy.deepcopy(matrix)
    if dirc=="right":
        for i in range(m):
            newrow=add(new[i])
            new[i]=newrow
    elif dirc=="down":
        for j in range(n):
            temp=[new[i][j] for i in range(m)]
            newline=add(temp)
            for k in range(m):
                new[k][j]=newline[k]
    elif dirc=="left":
        for i in range(m):
            temp=[new[i][j] for j in range(n-1,-1,-1)]
            newrow=add(temp)
            for k in range(n):
                new[i][n-1-k]=newrow[k]
    else:
        for j in range(n):
            temp=[new[i][j] for i in range(m-1,-1,-1)]
            newline=add(temp)
            for k in range(m):
                new[m-1-k][j]=newline[k]
    return new
result=0
def calculate(matrix,num):
    global result
    if num==p:
        result=max(result,max(max(matrix[i]) for i in range(m)))
        return
    calculate(move(matrix,"up"),num+1)
    calculate(move(matrix,"down"),num+1)
    calculate(move(matrix,"left"),num+1)
    calculate(move(matrix,"right"),num+1)
calculate(matrix,0)
print(result)
```



代码运行截图

![image-20231226092155978](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231226092155978.png)

### 27401: 最佳凑单

dp, sparse bucket, http://cs101.openjudge.cn/practice/27401/



思路：



##### 代码

```python
'''
刘思瑞 2100017810
'''
import sys
n,t = map(int,input().split())
value = list(map(int,input().split()))
total_value = sum(value)
if total_value  < t:
    print(0)
    sys.exit()
dp = []
for i in range(n+1):
    dp.append([0] + [-float("inf")]*(total_value))
for i in range(1,n+1):
    for j in range(1,total_value+1):
        if value[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i - 1][j - value[i - 1]] + value[i - 1])
for k in range(t,total_value+1):
    if dp[n][k] > 0:
        print(dp[n][k])
        sys.exit()
print(0)
```



代码运行截图

![image-20231226072510950](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231226072510950.png)





### 27384: 候选人追踪

heap, http://cs101.openjudge.cn/practice/27384/

熊江凯，这题应该不超纲的，感觉还是挺好的



思路：

直接看题解

##### 代码

```python
n,k = map(int,input().split())
lst = list(map(int,input().split()))
arr = sorted([[lst[2*i],lst[2*i+1]] for i in range(n)])
vote = [0 for _ in range(314160)]
s = list(map(int,input().split()))
mark_dict = {}
for i in range(k):
    mark_dict[s[i]] = 0
if k == 314159:
    print(arr[-1][0])
    exit()
most,least = 0,0
ans = 0
for j in range(n):
    v = arr[j][1]
    if v in mark_dict:
        mark_dict[v] += 1
        if least == mark_dict[v]-1:
            least = min(mark_dict.values())
    else:
        vote[v] += 1
        most = max(most,vote[v])
    if j < n-1 and arr[j+1][0] != arr[j][0] and least > most:
        ans += arr[j+1][0]-arr[j][0]
print(ans)
```



代码运行截图

![image-20231226073036609](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231226073036609.png)



### CF1883D. In Love

data structure, greedy, 1500, https://codeforces.com/problemset/problem/1883/D

黄源森、查达闻推荐



思路：



##### 代码

```python
out = []
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    if a[0] == n:
        x = n - 1
    else:
        x = n
    f = 0
    for i in range(n):
        if a[i] == x:
            f = i
        if f:
            b.append(a[i])
    if not f:
        b.append(a[0])
    if f == n - 1:
        f -= 1
    else:
        b.append(a[f - 1])
        f -= 2
 
    while f > 0 and a[f] > a[0]:
        b.append(a[f])
        f -= 1
    for i in range(f + 1):
        b.append(a[i])
    out.append(b)
 
for l in out:
    print(*l)
```



代码运行截图

![image-20231226090923945](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231226090923945.png)

## 2. 学习总结和收获

dp和搜索基本能够掌握这个套路了，但是到时候能不能过真不好说



