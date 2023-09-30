grade_minus, num = map(int,input().split())
price_o=[]
grade=[]
list_num=[]
need=[]
for i in range(num):
    a,b,c=map(int,input().split())
    price_o.append(a)
    grade.append(b)
    list_num.append(c)
    for i in range(c):
        d,e=map(int,input().split())
        need.append([d,e])

