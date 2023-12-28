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