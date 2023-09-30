"""
刘思瑞 2100017810
"""

num = int(input())
if num%2 != 0:
    print("0 0")
else:
    a = num//4 + (num%4)/2
    b = num/2
    print(str(int(a))+" "+str(int(b)))