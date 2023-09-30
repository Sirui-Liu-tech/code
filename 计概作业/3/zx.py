'''
刘思瑞 2100017810
'''
zero = [0]*6
while True:
    sum = 0
    goods = list(map(int,input().split()))
    if goods == zero:
        break
    sum += goods[5] + goods[4] + goods[3]
    if 11 * goods[4] <= goods[0]:
        goods[0] -= 11 * goods[4]
    else:
        goods[0] = 0
    if 5 * goods[3] <= goods[1]:
        goods[1] -= 5 * goods[3]
    elif 4 * (5 * goods[3] - goods[1]) <= goods[0]:
        goods[0] -= 4 * (5 * goods[3] - goods[1])
        goods[1] = 0
    else:
        goods[0] = 0
        goods[1] = 0
    sum += goods[2] // 4 +1
    goods[2] = goods[2] %4
    if goods[2] == 3:
        if goods[1] == 0:
            if goods[0] <= 9:
                goods[0] = 0
            else:
                goods[0] -= 9
        else:
            goods[1] -= 1
            if goods[0] <= 5:
                goods[0] = 0
            else:
                goods[0] -= 5
    elif goods[2] == 2:
        if goods[1] <= 3:
            goods[1] = 0
            if goods[0] <= 18 - 4 * goods[1]:
                goods[0] = 0
            else:
                goods[0] -= 18 - 4 * goods[1]
        else:
            goods[1] -= 3
            if goods[0] <= 6:
                goods[0] = 0
            else:
                goods[0] -= 6
    elif goods[2] == 1:
        if goods[1] <= 5:
            goods[1] = 0
            if goods[0] <= 27 - 4 * goods[1]:
                goods[0] = 0
            else:
                goods[0] -= 27 - 4 * goods[1]
        else:
            goods[1] -= 5
            if goods[0] <= 7:
                goods[0] = 0
            else:
                goods[0] -= 7
    else:
        sum -= 1
    sum += goods[1]//9 +1
    goods[1] = goods[1] % 9
    if goods[1] == 0:
        sum += -(-goods[0]//36)
        sum -= 1
    if goods[0] > 36 - goods[1] * 4:
        sum += -(-(goods[0] - (36 - goods[1] * 4))//36)
    print(sum)

