

def exchange(t):
    global d
    minnum = t[0] - d
    maxnum = t[0] + d
    num_min = t[0]
    index = 0
    for i in range(len(t)-1):
        if t[i] - d > minnum:
            minnum = t[i] -d
        if t[i] + d < maxnum:
            maxnum = t[i] + d
        if maxnum < minnum:
            break
        if (t[i+1] >= minnum) and (t[i+1] <= maxnum):
            if t[i+1] <= num_min:
                num_min = t[i+1]
                index = i+1 
    return  index

num , d = map(int, input().split())
hight = []

for i in range(num):
    hight.append(int(input()))

for i in range(num):
    index = exchange(hight)
    print(hight[index])
    del hight[index]