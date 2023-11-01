# Assignment #7: 贪心和DP

Updated 0919 GMT+8 Oct 24, 2023

2023 fall, Complied by ==同学的姓名、院系==



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++/C（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

4）如果不能在截止前提交作业，请写明原因。

另外，CF的题目，在洛谷有中文翻译，例如 https://www.luogu.com.cn/problem/CF1764C 



**编程环境**

==（请改为同学的操作系统、编程环境等）==

操作系统：macOS Ventura 13.4.1 (c)

Python编程环境：Spyder IDE 5.2.2, PyCharm 2023.1.4 (Professional Edition)

C/C++编程环境：Mac terminal vi (version 9.0.1424), g++/gcc (Apple clang version 14.0.3, clang-1403.0.22.14.1)



## 1. 必做题目

#### 158B. Taxi

*special problem, greedy, implementation, 1100

 https://codeforces.com/problemset/problem/158/B



思路：

贪心

##### 代码

```python
'''
刘思瑞 2100017810
'''
sum = 0
a = [0]*4
n = int(input())
for i in map(int,input().split()):
    a[i-1] += 1
sum += a[3]+a[2]
if a[0] <= a[2]:
    a[0] = 0
else:
    a[0] -= a[2]
sum += a[1] // 2
a[1] = a[1]%2
if a[1]:
    sum+=1
    if a[0] <= 2:
        a[0] = 0
    else:
        a[0] -= 2
sum += a[0]//4
if a[0] %4:
    sum += 1
print(sum)
```



代码运行截图

![image-20231031170435664](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231031170435664.png)

#### 545D. Queue

greedy, implementation, sortings, 1300

https://codeforces.com/problemset/problem/545/D



思路：



##### 代码

```python
'''
刘思瑞 2100017810
'''
sum = 0
n = int(input())
l = list(map(int,input().split()))
l.sort()
for i in l:
    if i >= sum:
        sum += i
    else:
        n -= 1
print(n)
```



代码运行截图

![image-20231031172511253](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231031172511253.png)

#### 803A. Maximal Binary Matrixcon

constructive algorithms, 1400

 https://codeforces.com/problemset/problem/803/A



思路：

先按字典序的一层一层填满，填不满时考虑奇偶性，看是否需要再往下一层的对角元

##### 代码

```python
'''
刘思瑞 2100017810
'''
def build(n,k):
    if k > n ** 2:
        print(-1)
        return
    a = []
    m = 0
    for i in range(n):
        a.append([0]*n)
    while True:
        if k == 0:
            for i in a:
                for j in i:
                    print(j,end=' ')
                print('')
            return
        if k >= 2*n - 2*m - 1 :
            for i in range(2*n - 2*m - 1):
                    a[m][i + n - 1 -(2*n - 2*m - 2)] ,a[i + n - 1 -(2*n - 2*m - 2)][m] = 1,1
            k -= 2*n - 2*m - 1 
            m+=1
        else:
            a[m][m] = 1
            k -= 1
            if k%2:
                a[m+1][m+1] = 1
            k = k//2
            for i in range(k):
                a[m][i + m + 1], a[i+m+1][m] = 1,1
            k = 0

n , k = map(int,input().split())
build(n,k)
```



代码运行截图 

![image-20231031215125989](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231031215125989.png)

#### 1793C. Dora and Search

constructive algorithms, data structures, two pointers, 1200, 

https://codeforces.com/problemset/problem/1793/C



思路：

不停判断两端是否为最值，建立活动窗口来删除元素

##### 代码

```python
'''
刘思瑞 2100017810
'''
def find(n,l):
    maxx = n
    minn = 1
    r = 0 
    p = n-1
    while minn<maxx:
        if l[r] == minn:
            minn += 1
            r += 1
        if l[p] == minn:
            p-= 1
            minn += 1
        if l[r] == maxx:
            maxx -= 1
            r += 1
        if l[p] == maxx:
            p-= 1
            maxx -= 1
        if (l[p] not in (maxx,minn)) and (l[r] not in (maxx,minn)):
            return r+1,p+1
    return -1,None
testnum = int(input())
for i in range(testnum):
    n = int(input())
    li = list(map(int,input().split()))
    l = li[:]
    maxx,minx = find(n,l)
    if minx:
        print(maxx,minx)
    else:
        print(-1)
```



代码运行截图 

![image-20231031225858363](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231031225858363.png)

## 2. 选做题目

#### 368B. Sereja and Suffixes

data structures, dp, 1100

https://codeforces.com/problemset/problem/368/B



思路：



##### 代码

```python
# 

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





#### 1764C. Doremy's City Construction

graphs, greedy, 1400

https://codeforces.com/problemset/problem/1764/C



思路：



##### 代码

```python
# 

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





## 3. 学习总结和收获

这周是期中周来不及写选座了，下周一起补上。感觉虽然对一些算法不是很熟练，但是对语法已经基本掌握了，不会出现特别低级的bug了



