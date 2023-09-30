"""
刘思瑞 2100017810
"""
sen = input()
sen_o = ''
for i in sen:
    if ord(i) >= 97 and ord(i) <= 122:
        i = chr(ord(i) - 32)
    elif ord(i) >= 65 and ord(i) <= 90:
        i = chr(ord(i) + 32)
    sen_o = sen_o + i
print(sen_o) 
