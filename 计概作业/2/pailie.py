'''
刘思瑞 2100017810
'''
def next(a):
    a = a[::-1]
    for i in range(len(a)-1):
        if a[i+1] < a[i]:
            minum = a[i]
            index = i
            for j in range(i+1):
                if a[j] > a[i+1] and a[j] < minum:
                    minum = a[j]
                    index = j
            b = a[:i+2]
            del b[index]
            b.sort(reverse = True)
            c = b + [minum] + a[i+2:]
            return c[::-1]
    return a

num = int(input())
for i in range(num):
    n , k = map(int, input().split())
    a = list(map(int, input().split()))
    for j in range(k):
        a = next(a)
    for j in range(n):
        print(a[j],end = ' ')
    print()

