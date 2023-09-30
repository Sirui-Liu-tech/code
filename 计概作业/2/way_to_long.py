def reduce(s):
    if len(s) > 10:
        return s[0] + str(len(s) - 2) + s[-1]
    else:
        return s

n =  int(input())
for i in range(n):
    print(reduce(input()))