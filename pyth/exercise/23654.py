'''
刘思瑞 2100017810
'''
sum = 0
inn = input()
year = []
for i in inn:
    sum += int(i)
    year.append(int(i))
if sum < 20:
    if 20 - sum <= 9 - year[3]:
        year[3] = year[3]+20-sum
    elif (20 - sum) - (9 - year[3]) <= 9 - year[2]:
        year[2] = year[2]+(20 - sum) - (9 - year[3])
        year[3] = 9
    else:
        year = [1,1,9,9]
elif sum > 20:
    if year[2] != 9:
        if sum - 20 <= year[3] - 1:
            year[2] = year[2]+1
            year[3] = year[3] -1 - sum +20 
        elif year[1] != 9:
            year[1] = year[1]+1
            if 20 - year[0] -year[1] <= 9:
                year[2] = 0
                year[3] = 20 - year[0] - year[1]
            else:
                year[3] = 9
                year[2] =20 - year[0] - year[1]-9      
        elif year[1] == 9:
            year[0] = year[0]+1
            year[3] = 9
            year[2] =20 - year[0] - 9
            year[1] =0 
    elif year[2] == 9:
        if year[1] != 9:
            year[1] = year[1]+1
            if 20 - year[0] -year[1] <= 9:
                year[2] = 0
                year[3] = 20 - year[0] -year[1]
            else:
                year[3] = 9
                year[2] =20 - year[0] -year[1]-9
        elif year[1] == 9:
            year[0] = year[0]+1
            year[3] = 9
            year[2] = 20 - year[0] - 9
            year[1] = 0
else:
    if year[2] != 9 and year[3] != 0:
        year[2] = year[2]+1
        year[3] = year[3]-1
    else:
        if year[1] != 9:
            year[1] = year[1]+1
            if 20 - year[0]- year[1] <= 9:
                year[3] = 20 - year[0] - year[1]
                year[2] = 0
            else:
                year[3] = 9
                year[2] = 20 -year[0] - year[1]-9
        else:
            year[0] += 1
            year[3] = 9
            year[2] = 20 -year[0] -9
            year[1] = 0
print(str(year[0])+str(year[1])+str(year[2])+str(year[3]))
        
