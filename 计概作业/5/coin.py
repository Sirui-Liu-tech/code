'''
刘思瑞 2100017810
'''
n = int(input())
coin = list(map(int,input().split()))
coin.sort(reverse=True)
summ = sum(coin)
half = summ//2 
num = 0
sumcoin = 0
for i in coin:
    sumcoin += i
    num += 1
    if sumcoin > half:
        break
print(num)