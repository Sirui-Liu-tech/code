from math import sqrt
import sys
def pFactors(n):
    """Finds the prime factors of 'n'"""
    pFact, limit, check, num = [], int(sqrt(n)) + 1, 2, n
    for check in range(2, limit):
        while num % check == 0:
            pFact.append(check)
            num /= check
    if num > 1:
        pFact.append(num)
    return pFact 
n = int(input())
l = pFactors(n)
for i in range(len(l)-1):
    if l[i] == l[i+1]:
        print(0)
        sys.exit()
if len(l) %2 == 0:
    print(1)
else:
    print(-1)