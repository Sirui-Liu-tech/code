while True:
    try:
        t = 1
        code=input()
        if not code:
            break
        code=code.lstrip()
        flag=1

        if code[0] in ["@","."]:
            flag=0
        elif code[-1] in ["@","."]:
            flag=0
        
        sum=0
        for _ in code:
            if _ =="@":
                sum+=1

        if sum!=1:
            flag=0

        for i in range(len(code)):
            if code[i]=="@":
                t=i

        if code[t+1]==".":
            flag=0
        if t-1 >= 0:
            if code[t-1]==".":
                flag=0

        times=0
        for j in range(t+1,len(code)):
            if code[j]==".":
                times+=1
            
        if times==0:
            flag=0   

        if flag==1:
            print("YES")
        else:
            print("NO")

    except:
        break