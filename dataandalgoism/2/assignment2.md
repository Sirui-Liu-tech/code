# Assignment #2: 编程练习

Updated 0953 GMT+8 Feb 24, 2024

2024 spring, Complied by 刘思瑞 元培学院



**说明：**

1）The complete process to learn DSA from scratch can be broken into 4 parts:
- Learn about Time and Space complexities
- Learn the basics of individual Data Structures
- Learn the basics of Algorithms
- Practice Problems on DSA

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知3月1日导入选课名单后启用。**作业写好后，保留在自己手中，待3月1日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

操作系统：Windows 11 22H2 22621.2283

Python编程环境：Visual Studio (1.82.2); python 3.11.3

C/C++编程环境：无



## 1. 题目

### 27653: Fraction类

http://cs101.openjudge.cn/practice/27653/



思路：

正常写类

##### 代码

```python
'''
2100017810 刘思瑞
'''
import math

class fraction:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self,m):
        c = self.b * m.b
        d = self.a * m.b + self.b *m.a
        e = math.gcd(c,d)
        f = c//e
        g = d//e
        return fraction(g,f)
    def output(self):
        print('%d/%d' %(self.a ,self.b))

a,b,c,d = map(int,input().split())
p = fraction(a,b)
q= fraction(c,d)
(p.add(q)).output()
```



代码运行截图

![image-20240305162356623](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20240305162356623.png)





### 04110: 圣诞老人的礼物-Santa Clau’s Gifts

greedy/dp, http://cs101.openjudge.cn/practice/04110



思路：

贪心，排序一下

##### 代码

```python
'''
刘思瑞 2100017810
'''
n , w0 = map(int,input().split())
record = []
for i in range(n):
    v , w = map(int,input().split())
    record.append([v/w,v,w])
for i in range(n-1):
    for j in range(n-1-i):
        if record[j][0] < record[j+1][0]:
            record[j] , record[j+1] = record[j+1] , record[j]
sum = 0
for i in record:
    if i[2] < w0:
        sum+= i[1]
        w0 -= i[2]
    else:
        sum+= i[0] * w0
        break
print('%.1f' % sum)
```



代码运行截图

![image-20240305162516539](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20240305162516539.png)





### 18182: 打怪兽

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/



思路：

排序

##### 代码

```python
'''
刘思瑞 2100017810
'''
testnum = int(input())
for i in range(testnum):
    n ,m ,b = map(int,input().split())
    release = []
    time = []
    flag = 1
    for j in range(n):
        t , hurt = map(int,input().split())
        if t in time:
            release[time.index(t)].append(hurt)
        else:
            time.append(t)
            release.append([hurt])
    l = len(time)
    for j in range(l-1):
        for k in range(l-1-j):
            if time[k] > time[k+1]:
                time[k] , time[k+1] , release[k] , release[k+1] = time[k+1] , time[k] , release[k+1] , release[k]
    for j in range(l):
        release[j].sort(reverse = True)
        hurting = sum(release[j][:m])
        if hurting >= b:
            print(time[j])
            flag = 0
            break
        else:
            b -= hurting
    if flag:
        print('alive')
```



代码运行截图 

![image-20240305162550430](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20240305162550430.png)



### 230B. T-primes

binary search/implementation/math/number theory, 1300, http://codeforces.com/problemset/problem/230/B



思路：

欧拉筛

##### 代码

```python
'''
刘思瑞 2100017810
'''
def euler(n):
    filter, primers = [False for i in range(n + 1)], []
    for i in range(2, n + 1):
        if not filter[i]:
            primers.append(i)
        for prime in primers:
            if i * prime > n:
                break
            filter[i * prime] = True
            if i % prime == 0:
                break
    return filter
 
def search(num):
    global prime_
    sq = int(num**(0.5))
    if int(sq**2) != num or num == 1:
        return 'NO'
    if not prime_[sq]:
        return 'YES'
    return 'NO'
 
n = int(input())
num = list(map(int,input().split()))
n = int(max(num)**(0.5))
prime_ = euler(n)
for i in num:
    print(search(i))
```



代码运行截图

![image-20240305162646616](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20240305162646616.png)





### 1364A. XXXXX

brute force/data structures/number theory/two pointers, 1200, https://codeforces.com/problemset/problem/1364/A



思路：

可以说明一定是从两侧开始计算最长

##### 代码

```python
    '''
    刘思瑞 2100017810
    '''
    def calcu(le,x,array):
        nonzero = []
        for i in range(le):
            array[i] %= x
            if array[i] != 0:
                nonzero.append(i)
        sum = -1
        if len(nonzero) ==0:
            return sum
        if len(nonzero) ==1:
            return le
        sum = nonzero[0] +1
        nsum = 0
        for j in range(0,len(nonzero)):
            nsum += array[nonzero[j]]
            if nsum % x != 0:
                if j+1 < len(nonzero):
                    if nonzero[j+1] >sum:
                        sum = nonzero[j+1]
                else:
                    return le
        return sum
     
     
    n = int(input())
    for i in range(n):
        le , x = map(int,input().split())
        array = list(map(int,input().split()))
        print(max(calcu(le,x,array),calcu(le,x,array[::-1])))
```



代码运行截图 

![image-20240305165930864](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20240305165930864.png)



### 18176: 2050年成绩计算

http://cs101.openjudge.cn/practice/18176/



思路：

欧拉筛

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

![image-20240305165958687](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20240305165958687.png)



## 2. 学习总结和收获

还是上学期的练习题，每日选座做了一些





