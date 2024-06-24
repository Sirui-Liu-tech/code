'''
2100017810 刘思瑞
'''
def is_rational(s,m):
    stack = []
    if len(m) != len(s):
        return False
    while True:
        if not m:
            return True
        yemp = m.pop()
        while (not stack or stack[-1] != yemp) and s:
            stack.append(s.pop(0))
        if not stack or stack[-1] != yemp:
            return False
        stack.pop()

s = [i for i in input().strip()]
out = {True:'YES',False:'NO'}
while True:
    try:
            m = [i for i in input().strip()]
            print(out[is_rational(s[::],m[::-1])])
    except EOFError:
        break

def is_valid_move(n, m, x, y, visited, new_x, new_y):
    return 0 <= new_x < n and 0 <= new_y < m and not visited[new_x][new_y]



