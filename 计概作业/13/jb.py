'''
刘思瑞 2100017810
'''
for _ in range(int(input())):
    L = [[],[],[]]
    flag = 0
    for i in range(3):
        L[i] = input().split()
    for f in 'ABCDEFGHIJKL':
        if all((f in i[0] and i[2]=='up') or (f in i[1] and i[2]=='down') 
               or ( f not in i[0] + i[1] and i[2]=='even') for i in L):
            flag = 'heavy'
            break
        if all((f in i[0] and i[2]=='down') or (f in i[1] and i[2]=='up') 
               or (f not in i[0]+i[1] and i[2]=='even') for i in L):
            flag = 'light'
            break
    print(f +" is the counterfeit coin and it is "+flag+ ".")