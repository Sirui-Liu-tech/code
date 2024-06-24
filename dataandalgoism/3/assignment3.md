# Assignment #3: March月考

Updated 1537 GMT+8 March 6, 2024

2024 spring, Complied by ==同学的姓名、院系==



**说明：**

1）The complete process to learn DSA from scratch can be broken into 4 parts:
- Learn about Time and Space complexities
- Learn the basics of individual Data Structures
- Learn the basics of Algorithms
- Practice Problems on DSA

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

==（请改为同学的操作系统、编程环境等）==

操作系统：macOS Ventura 13.4.1 (c)

Python编程环境：Spyder IDE 5.2.2, PyCharm 2023.1.4 (Professional Edition)

C/C++编程环境：Mac terminal vi (version 9.0.1424), g++/gcc (Apple clang version 14.0.3, clang-1403.0.22.14.1)



## 1. 题目

**02945: 拦截导弹**

http://cs101.openjudge.cn/practice/02945/



思路：

dp

##### 代码

```python
'''
2100017810 刘思瑞
'''
num = int(input())
m = list(map(int,input().split()))
count =   1  
dp = [0]*num
for i in range(num):
    temp = [1]
    for j in range(i):
        if m[i] <= m[j] :
            temp.append(dp[j]+1)
            if dp[j] + 1 >count:
                count = dp[j] + 1
    dp[i] = max(temp)

print(max(dp))
```



代码运行截图 、

![image-20240312152408541](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20240312152408541.png)



**04147:汉诺塔问题(Tower of Hanoi)**

http://cs101.openjudge.cn/practice/04147



思路：



##### 代码

```python
num,a,b,c = input().split()
num =int(num)
pin = [a,b,c]
def outputt(n,a,b):
    global pin
    print('%d:%s->%s' %(n,pin[a],pin[b]))
def secp(a,b):
    m = [0,1,2]
    m.remove(a)
    m.remove(b)
    return m[0]
    
def move(num,a,b):
    if num == 0:
        return
    move(num-1,a,secp(a,b))
    outputt(num,a,b)
    move(num-1,secp(a,b),b)
    return

move(num,0,2)
```



代码运行截图

![image-20240312193237166](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20240312193237166.png)





**03253: 约瑟夫问题No.2**

http://cs101.openjudge.cn/practice/03253



思路：

链表

##### 代码

```python
'''
2100017810 刘思瑞
'''
class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None

class ysf(object):
    def __init__(self):
        self.head = None
    def is_empty(self):
        if self.head:
            return False
        else:
            return True
    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = node
            node.next = self.head

while True:
    n,p,m = map(int,input().split())
    if (n,p,m) == (0,0,0):
        break
    ysfi = ysf()
    for i in range(1,n+1):
        ysfi.append(i)
    begin = ysfi.head
    if p !=1:
        for i in range(p-2):
            begin = begin.next
    else:
        for i in range(n-1):
            begin = begin.next
    for j in range(n-1):
        for i in range(m-1):
            begin = begin.next
        print(begin.next.item,end=',')
        begin.next = begin.next.next
    begin = begin.next
    print(begin.item)
```



代码运行截图 

![image-20240312200634530](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20240312200634530.png)



**21554:排队做实验 (greedy)v0.2**

http://cs101.openjudge.cn/practice/21554



思路：

贪心

##### 代码

```python
n = int(input())
li = list(map(int,input().split()))
bi = [[li[i],i] for i in range(n)]
bi = sorted(bi,key = lambda x: x[0])
for i in bi:
    print(i[1]+1,end=' ')
print()
summ = 0
for i in range(0,n):
    summ+= (n-1-i)*bi[i][0]
print('%.2f' %(summ/n))
```



代码运行截图

![image-20240312200729848](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20240312200729848.png)





**19963:买学区房**

http://cs101.openjudge.cn/practice/19963



思路：

去年月考的题，就正常的操作题目

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

![image-20240312200904259](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20240312200904259.png)



**27300: 模型整理**

http://cs101.openjudge.cn/practice/27300



思路：

默认字典

##### 代码

```python
'''
2100017810 刘思瑞
'''
from collections import defaultdict
n = int(input())
d = defaultdict(list)
e = {'M':1,'B':1000}
for i in range(n):
    name, attribute = input().split('-')
    d[name].append(attribute)
kkk = d.keys()
kkk = list(kkk)
kkk.sort()
for i in kkk:
    d[i].sort(key= lambda x: float(x[:-1])* e[x[-1:]])
    print(i+":",end=' ')
    for j in range(len(d[i])-1):
        print(d[i][j],end=', ')
    print(d[i][len(d[i])-1])
```



代码运行截图

![image-20240312202436393](C:\Users\86189\AppData\Roaming\Typora\typora-user-images\image-20240312202436393.png)

## 2. 学习总结和收获

大部分还是做过的题目，每日选做大概一周会做两三天的题目





