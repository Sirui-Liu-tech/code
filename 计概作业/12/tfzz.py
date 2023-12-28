'''
2100017810 刘思瑞
'''
L,n,m = map(int,input().split())
rock = [0]
for i in range(n):
    rock.append(int(input()))
rock.append(L)
def check(p):
    num = 0
    N = 0
    for i in range(1, n+2):
        if rock[i] - N <p:
            num += 1
            if num > m:
                return True
        else:
            N = rock[i]
    if num > m:
        return True
    else:
        return False

low, high = 0, L+1
ans = -1
while low < high:
    mid = (low + high) // 2
    if check(mid):
        high = mid
    else: 
        ans = mid 
        low = mid + 1
print(ans)