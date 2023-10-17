'''
刘思瑞 2100017810
'''
def calcu(calculate,i,j):
    global calcull
    if calculate[i+1] not in calcull:
        if calculate[i+2] not in calcull:
            calculate[i] = str(eval(calculate[i+1]+calculate[i]+calculate[i+2]))
            del calculate[i+1]
            del calculate[i+1]
            i = j[-1]
            j = j[:-1]
        else:
            j.append(i)
            i = i+2
    else:
        j.append(i)
        i = i+1
    return calculate, i, j
    

calcull = ['+','-','*','/']
calculate = list(input().split())
i = 0
j = [0]
while True:
    calculate, i ,j = calcu(calculate,i,j)
    if len(calculate) == 1:
        break
print('%.6f' % float(calculate[0]))