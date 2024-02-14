import win32com.client

from tqdm import tqdm 

a=[]

b=[]

c=[]

ProtectPass=[]

for i in range(2048):

    a.append(list('{:011b}'.format(i))) #生成2^11次的组合列表，因为11位密码有2^11种排列组合方式，将排列组合列表作为成员添加到列表中，此时生成的是二进制0和1

#print(a)

for i in a: # 遍历列表中的所有组合

    for j in i: # 对排列组合列表中的各个成员值进行遍历

        b.append(int(j)+65) # 对各个成员进行加65操作 0加65等于本身 1加65=66

    c.append(b) # 生成包含65和66的所有排列可能

    b=[]

for k in c: # 对所有的排列可能进行遍历 得到每组排列组合的列表形式

    #print(k)

    m=list(k) # 转换成列表

    m.append(0) #末尾再加一组成员0，因为要对其进行复制，末尾成员的值范围不是65或者66

    for n in range(32,127):

        m[len(m)-1]=n #末尾成员的赋值，范围是32-126

        #print(m)

        list2=[chr(i) for i in m] #将int类型转化成ascii码，也就是字符

        str=''.join(list2) #将字符列表转成字符串

        ProtectPass.append(str) # 最后将每一串字符串作为列表成员放入列表 方便破解密码

xlsx=win32com.client.Dispatch('Excel.Application') # 获得Excel对象



# 如果是需要跑活动工作表的密码 可以使用 wb.ActiveSheet

for EditPass in tqdm(ProtectPass):

    try:

        wb=xlsx.Workbooks.Open('C:/Users/86189/Desktop/a.xlsx',False,False,None,Password=EditPass)

        print(f"成功了 密码是{EditPass}") # 成功以后则直接跳出

        break

    except: # 出现异常就代表密码错误  此时需要无视异常继续试下一个密码

        continue
