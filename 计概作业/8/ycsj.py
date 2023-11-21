'''
刘思瑞 2100017810
'''
n , m = map(int,input().split())
grade = list(map(int,input().split()))
grade.sort()
minusgrade = []
separa = [0]
sum = grade[-1] - grade[0]
for i in range(n-1):
    minusgrade.append(grade[i+1]-grade[i])
minusgrade.sort(reverse=True)
for i in range(m-1):
    sum -= minusgrade[i]
print(sum)