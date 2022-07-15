N, M = map(int, input().split())
n = list(range(N+1, 0, -1))
string = ''

a = n.pop()

print(a)


for i in range(1, N+1):
    string[0] = i

    str2 = ''
    for x in range(1, M+1):
        str2[x] = a
    string += str2 + '\n'
        