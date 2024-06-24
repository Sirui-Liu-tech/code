# Assignment #1: 拉齐大家Python水平

Updated 0940 GMT+8 Feb 19, 2024

2024 spring, Complied by 刘思瑞 元培学院



**说明：**

1）数算课程的先修课是计概，由于计概学习中可能使用了不同的编程语言，而数算课程要求Python语言，因此第一周作业练习Python编程。如果有同学坚持使用C/C++，也可以，但是建议也要会Python语言。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知3月1日导入选课名单后启用。**作业写好后，保留在自己手中，待3月1日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

操作系统：Windows 11 22H2 22621.2283

Python编程环境：Visual Studio (1.82.2); python 3.11.3

C/C++编程环境：无





## 1. 题目

### 20742: 泰波拿契數

http://cs101.openjudge.cn/practice/20742/



思路：

正常递推

##### 代码

```python
'''
2100017180 刘思瑞
'''
n = int(input())
a,b,c = 0,1,1
for i in range(n-2):
    a,b,c = b,c,a+b+c
print(c)
```



代码运行截图

![image-20240220193001482](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20240220193001482.png)





### 58A. Chat room

greedy/strings, 1000, http://codeforces.com/problemset/problem/58/A



思路：

正则表达式，上学期做过好像

##### 代码

```python
'''
刘思瑞 2100017810
'''
import re
word = input()
if re.search('h.*e.*l.*l.*o',word):
    print('YES')
else:
    print('NO')
```



代码运行截图

![image-20240220193420573](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20240220193420573.png)



### 118A. String Task

implementation/strings, 1000, http://codeforces.com/problemset/problem/118/A



思路：

上学期做过就正常写

##### 代码

```python
'''
刘思瑞 2100017810
'''
s = input()
re = ['a','e','i','o','u','y']
s = s.lower()
for i in re:
    s = s.replace(i,'')
for i in s:
    print('.'+ i,end = '')
```



代码运行截图

![image-20240220193546358](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20240220193546358.png)





### 22359: Goldbach Conjecture

http://cs101.openjudge.cn/practice/22359/



思路：

欧拉筛

##### 代码

```python
'''
2100017180 刘思瑞
'''
N = int(input())
isprime =[False] + [True for i in range(N+1)]
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
euler()
for i in range(N):
    if isprime[i] and isprime[N-i]:
        print(i,N-i)
        break 
```



代码运行截图 

![image-20240220194636187](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20240220194636187.png)





### 23563: 多项式时间复杂度

http://cs101.openjudge.cn/practice/23563/



思路：

正常做就好

##### 代码

```python
'''
刘思瑞 2100017810
'''
max = 0
s = list(input().split('+'))
for i in s:
    j = list(i.split('n^'))
    if j[0] != '0':
        if int(j[1]) > max:
            max = int(j[1])
print('n^'+str(max)) 
```



代码运行截图

![image-20240220195415015](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20240220195415015.png)



### 24684: 直播计票

http://cs101.openjudge.cn/practice/24684/



思路：

默认键值字典

##### 代码

```python
'''
2100017180 刘思瑞
'''
import collections
d = collections.defaultdict(int)
for i in list(map(int,input().split())):
    d[i] += 1
result= []
maxx = max(d.values())
for k,v in d.items():
    if v == maxx:
        result.append(k)
result.sort()
for i in result:
    print(i,end=' ')
```



代码运行截图

![image-20240220200907036](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20240220200907036.png)



## 2. 学习总结和收获

上学期正好学的是闫老师的计算概论所以这些题目基本上也都做过了，这周就做了一些oj上面的每日选做。





