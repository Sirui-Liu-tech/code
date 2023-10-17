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

