# Assignment #A: 矩阵和动态规划

Updated 1406 GMT+8 Nov 14, 2023

2023 fall, Complied by 刘思瑞 2100017810



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

3）如果不能在截止前提交作业，请写明原因。



**编程环境**

操作系统：Windows 11 22H2 22621.2283

Python编程环境：Visual Studio (1.82.2); python 3.11.3

C/C++编程环境：无



## 1. 必做题目

### OJ12558: 岛屿周⻓

matices, http://cs101.openjudge.cn/practice/12558/



思路：

补齐一圈，直接遍历

##### 代码

```python
'''
刘思瑞 2100017810
'''
n ,m =map(int,input().split())
matrix = [[0]*(m+2)]
for i in range(n):
    matrix.append([0]+list(map(int,input().split()))+[0])
matrix.append([0]*(m+2))
c = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if matrix[i][j]:
            c += 4-(matrix[i+1][j]+matrix[i][j+1]+matrix[i][j-1]+matrix[i-1][j])
print(c)
```



代码运行截图

![image-20231121210621855](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231121210621855.png)

### OJ02760: 数字三角形

dp, http://cs101.openjudge.cn/practice/02760/



思路：

从下层遍历

##### 代码

```python
'''
刘思瑞 2100017810
'''
n = int(input())
matrix = []
maxx = 0
for i in range(n):
    matrix.append(list(map(int,input().split())))
temp = matrix[-1]
for i in range(n-1,0,-1):
    ttemp = []
    for j in range(i):
        ttemp.append(max(matrix[i-1][j]+temp[j],matrix[i-1][j]+temp[j+1]))
    temp = ttemp
print(temp[0])
```



代码运行截图

![image-20231121213651361](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231121213651361.png)

### OJ02773: 采药

dp, http://cs101.openjudge.cn/practice/02773



思路：

背包问题

##### 代码

```python
'''
刘思瑞 2100017810
'''
T,M = map(int,input().split())
li = []
value = 0
for i in range(M):
    t,m = map(int,input().split())
    li.append([t,m])
value = [[0]*(li[0][0]) + [li[0][1]]*(T+1-li[0][0])]
for i in range(len(li)-1):
    value.append([0]*(T+1))
for i in range(1,len(li)):
    for j in range(1,T+1):
        if j >= li[i][0]:
            value[i][j] = max(value[i-1][j],value[i-1][j-li[i][0]]+li[i][1])
        else:
            value[i][j] = value[i-1][j]
print(value[-1][-1])
```



代码运行截图 

![image-20231121224825306](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231121224825306.png)

### OJ18106: 螺旋矩阵

matrices, http://cs101.openjudge.cn/practice/18106/

这个题目技巧性较强，可以看题解记住。



思路：

设定一个方向，注意每两次换向会改变长度

##### 代码

```python
'''
刘思瑞 2100017810
'''
def change(sign):
    if sign == [0,-1]:
        return [-1,0]
    if sign == [-1,0]:
        return [0,1]
    if sign == [0,1]:
        return [1,0]
    if sign == [1,0]:
        return [0,-1]
n = int(input())
m = []
for i in range(n):
    m.append([0]*n)
for i in range(n):
    m[0][i] = i+1
i = n
x = n-1
y = 0
sign = [0,-1]
for j in range(n-1,0,-1):
    for k in range(j):
        i+=1
        x , y = x+sign[0],y-sign[1]
        m[y][x] = i
    sign = change(sign)
    for k in range(j):
        i+=1
        x , y = x+sign[0],y-sign[1]
        m[y][x] = i
    sign = change(sign)
for i in m:
    for j in i:
        print(j,end=' ')
    print('')
```



代码运行截图

![image-20231121231034763](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231121231034763.png)

## 2. 选做题目

如果耗时太⻓，直接看解题思路，或者源码

### CF189A: Cut Ribbon

brute force/dp, 1300, https://codeforces.com/problemset/problem/189/A



思路：



##### 代码

```python
# 

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





### CF455A: Boredom

dp, 1500, https://codeforces.com/contest/455/problem/A



思路：



##### 代码

```python
# 

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





## 3. 学习总结和收获

期中周刚刚结束，以前感觉dp的题目有思路但是不好动笔，现在我发现最关键的是状态转移方程，只要能从数学上得到方程，就可以知道很关键的遍历顺序了。





