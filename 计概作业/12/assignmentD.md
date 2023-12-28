# Assignment #D: Dec 月考

Updated 1506 GMT+8 Dec 7, 2023

2023 fall, Complied by ==同学的姓名、院系==



**说明：**

1）Dec ⽉考： AC6==（请改为同学的通过数）== 。题⽬都在“练习”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

==（请改为同学的操作系统、编程环境等）==

操作系统：macOS Ventura 13.4.1 (c)

Python编程环境：Spyder IDE 5.2.2, PyCharm 2023.1.4 (Professional Edition)

C/C++编程环境：Mac terminal vi (version 9.0.1424), g++/gcc (Apple clang version 14.0.3, clang-1403.0.22.14.1)



## 1. 题目

如果耗时太⻓，直接看解题思路，或者源码



### 18176: 2050年成绩计算

http://cs101.openjudge.cn/practice/18176/



思路：



##### 代码

```python
'''
2100017810 刘思瑞
'''
N=10001
isprime = [True for i in range(N)]
prime= []
def euler():
    global N
    isprime[1]=False
    for i in range(2,N) :
        if isprime[i]:
            prime.append(i)
        for j in prime:
            if i*j>=N:
                break
            isprime[i*j] = False
            if i%j == 0:
                break

def calcu(grade):
    global isprime
    temp = []
    for i in grade:
        if i == int(i**0.5)**2:
            if isprime[int(i**0.5)]:
                temp.append(i)
    if temp == []:
        print('0')
        return
    print('%.2f' % (sum(temp)/len(grade)))
    return

euler()
m , n = map(int , input().split())
for i in range(m):
    calcu(list(map(int , input().split())))
```



代码运行截图

![image-20231212212544841](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231212212544841.png)





### 18224: 找魔数

http://cs101.openjudge.cn/practice/18224



思路：

遍历

##### 代码

```python
from math import sqrt

def search(n):
    q = int(sqrt(n/2))
    for i in range(1,q+1):
        p = n-i**2
        if p == int(sqrt(p))**2:
            print(bin(n),oct(n),hex(n))
            return
    return
    

m= int(input())
li = list(map(int,input().split()))
for i in li:
    search(i)
```



代码运行截图 

![image-20231212221410252](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231212221410252.png)





### 19963: 买学区房

http://cs101.openjudge.cn/practice/19963



思路：

直接计算

##### 代码

```python
summ = 0
n = int(input())
pairs = [i[1:-1] for i in input().split()]
distances = [ sum(map(int,j.split(','))) for j in pairs]
value = list(map(int,input().split()))
vxjjb = value[::]
vxjjb.sort()
if n %2 ==1:
    midv = vxjjb[(n-1)//2]
else:
    midv = (vxjjb[n//2]+vxjjb[n//2-1])/2
xjb = []
for i in range(n):
    xjb.append(distances[i]/value[i])
xjjb = xjb[::]
xjjb.sort()
if n %2 ==1:
    midxjb = xjjb[(n-1)//2]
else:
    midxjb = (xjjb[n//2]+xjjb[n//2-1])/2
for i in range(n):
    if xjb[i]>midxjb and value[i] < midv:
        summ+=1
print(summ)
```



代码运行截图 

![image-20231212221324208](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231212221324208.png)

### 23806: 三数之和

http://cs101.openjudge.cn/practice/23806/



思路：

双指针

##### 代码

```python
'''
2100017810 刘思瑞
'''
num = list(map(int,input().split()))
num.sort()
n = len(num)
record = set()
for i in range(n):
    if i != 0 :
        if num[i] == num[i-1]:
            continue
    low = i+1
    high = n - 1
    while low < high:
        if num[i] + num[low] + num[high] == 0:
            record.add((num[i],num[low],num[high]))
            high -= 1
            low+=1
        elif num[i] + num[low] + num[high] > 0:
            high -= 1
        else:
            low+=1
print(len(record))
```



代码运行截图



![image-20231212184523586](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231212184523586.png)

### 25561: 2022决战双十一

http://cs101.openjudge.cn/practice/25561/





思路：

直接硬干就行

##### 代码

```python
'''
2100017810 刘思瑞
'''
def value(buynumber):
    global boutique,maion
    boutiquevalue = [0]*m
    for i in range(n):
        boutiquevalue[buynumber[i]]+=(boutique[i][buynumber[i]])
    minusvalue = 0
    for i in range(m):
        summ = 0
        if boutiquevalue[i] != 0:
            for j in maion[i]:
                if j[1] > summ and j[0] <= boutiquevalue[i]:
                    summ = j[1]
        minusvalue += summ
    return sum(boutiquevalue) - (50*(sum(boutiquevalue)//300)) - minusvalue
def bianli(i,buynumber):
    global minn
    if i == n:
        minn = min(minn,value(buynumber))
        return
    for j in range(m):
        buynumber.append(j)
        bianli(i+1,buynumber)
        buynumber.pop()
    return
    
n,m = map(int,input().split())
boutique = []
maion = []
for i in range(n):
    part = list(input().split())
    _ = [10**6] * m
    for x in part:
        _[list(map(int,x.split(':')))[0]-1]= list(map(int,x.split(':')))[-1]
    boutique.append(_)
for i in range(m):
    part = list(input().split())
    _ = [list(map(int,x.split('-'))) for x in part]
    maion.append(_)
minn = value([0]*n)
bianli(0,[])
print(minn)
```



代码运行截图

![image-20231212205406678](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231212205406678.png)

### 08210: 河中跳房子

http://cs101.openjudge.cn/practice/08210/



思路：

二分查找

##### 代码

```python
'''
2100017810 刘思瑞
'''
L,n,m = map(int,input().split())
rock = [0]
for i in range(n):
    rock.append(int(input()))
rock.append(L)
def check(p):
    num = 0
    N = 0
    for i in range(1, n+2):
        if rock[i] - N <p:
            num += 1
            if num > m:
                return True
        else:
            N = rock[i]
    if num > m:
        return True
    else:
        return False

low, high = 0, L+1
ans = -1
while low < high:
    mid = (low + high) // 2
    if check(mid):
        high = mid
    else: 
        ans = mid 
        low = mid + 1
print(ans)
```



代码运行截图

![image-20231212215259831](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231212215259831.png)





### 01922: Ride to School

http://cs101.openjudge.cn/practice/01922/



思路：

在0之前出发的，如果会被追上说明肯定不是最早，因此只需要考虑0之后出发的，根据策略，只要是最快到达的就可以

##### 代码

```python
'''
2100017810 刘思瑞
'''
import math
while True:
    N = int(input())
    if N == 0:
        break
    summary = []
    for i in range(N):
        v,t = map(int,input().split())
        summary.append([t,t+(4.5/v)*3600,v])
    minn = 10**7
    for i in summary:
        if i[1]>0 and i[0]>=0:
            minn = min(minn,i[1])
    print(math.ceil(minn))
```



代码运行截图 

![image-20231212221127523](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20231212221127523.png)





## 2. 学习总结和收获

考试的时候感觉有思路并且写出来了，但是感觉这次题目比较复杂，好几个都debug没成功，回来再一看才发现问题，另一方面是第一题的时间卡的很慌。





