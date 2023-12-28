'''
刘思瑞 2100017810
'''
def money(tian,king,num):
    tian.sort(reverse=True)
    king.sort(reverse=True)
    sum = 0
    while True:
        if tian == []:
            print(sum*200)
            return
        besttian = tian[0]
        worsetian = tian[-1]
        bestking = king[0]
        worseking = king[-1]
        if worsetian > worseking:
            tian,king = tian[:-1],king[:-1]
            sum+=1
        elif worsetian < worseking:
            tian,king = tian[:-1],king[1:]
            sum-=1
        elif worseking == worsetian:
            if bestking < besttian:
                tian,king = tian[:-1],king[:-1]
            elif bestking > besttian:
                tian,king = tian[:-1],king[1:]
                sum-=1
            else:
                if worsetian < bestking:
                    sum-=1
                tian,king = tian[:-1],king[1:]
        
while True:
    n = int(input())
    if not n:
        break
    tian = list(map(int,input().split()))
    king = list(map(int,input().split()))
    money(tian,king,n)