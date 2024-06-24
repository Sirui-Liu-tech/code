def inp(s):
    import re
    s=re.split(r'([\(\)\+\-\*\/])',s)
    s=[item for item in s if item.strip()]
    return s

num = int(input())
for j in range(num):
    stack = []
    output = []
    dic = {'+':1,'-':1,'*':2,'/':2}
    for i in inp(input()):
        if not i in '+-*/()':
            output.append(i)
        else:
            if i == '(':
                stack.append(i)
            elif i == ')':
                while True:
                    if stack[-1] == '(':
                        stack.pop()
                        break
                    output.append(stack.pop())
            else:
                if not stack or stack[-1]=='(' or dic[i] > dic[stack[-1]]:
                    stack.append(i)
                else:
                    while True:
                        output.append(stack.pop())
                        if not stack or stack[-1]=='(' or dic[i] > dic[stack[-1]]:
                            stack.append(i)
                            break
    while stack:
        output.append(stack.pop())
    print(' '.join(output))