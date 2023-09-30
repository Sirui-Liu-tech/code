
def exchange(t):
    global d
    list1=[]
    for j in range(t[0]-d,t[0]+d+1):
        list1.append(j)
    min_num = 10**9
    i_0 = -1
    for i in range(len(t)-1):
        list_temp=[]
        if abs(t[i]-t[i+1]) > 2*d:
            break
        for j in range(t[i]-d,t[i]+d+1):
            if j in list1:
                list_temp.append(j)
        list1 = list_temp
        if t[i+1] in list1:
            if t[i+1] <= min_num:
                min_num = t[i+1]
                i_0 = i+1
        if not(list1):
            break
    return i_0

num , d = map(int, input().split())
hight = []
for i in range(num):
    hight.append(int(input()))

for i in range(num):
    index = exchange(hight)
    if index != -1:
        print(hight[index])
        for j in range(index,0,-1):
            hight[j] = hight[j-1]
        hight = hight[1:]
    else:
        print(hight[0])
        hight = hight[1:]