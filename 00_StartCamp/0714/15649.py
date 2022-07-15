# N, M = map(int, input().split())
N = 4
M = 4
lst = []

def dfs():
    print('dfs() called')
    print('current lst:', lst)
    if len(lst) == M:
        print(' '.join(map(str,lst)))
        return
    else:
        for i in range(1, N+1):
            print('i =', i)
            if i not in lst:
                print('append', i)
                lst.append(i)
                dfs()
                pop = lst.pop()
                print('popped', pop)
    print('dfs() exited')
dfs()