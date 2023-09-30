'''
刘思瑞 2100017810
'''
row = 0
for i in range(5):
    m = list(map(int,input().split()))
    if 1 in m:
        col = m.index(1)
        row_ =row
    row += 1
print(abs(row_-2)+abs(col-2))