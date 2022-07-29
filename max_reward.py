def view(a):
    if lst[a] == lst2[a]:
        view(a + 1)
    else:
        lst[a] = lst2[a]

T = int(input())
for t in range(1, T + 1):
    lst1, N = map(str, input().split())
    lst = list(lst1)
    lst2 = sorted(lst, reverse = True)

    for i in range(int(N)):
        view(i)
    print(''.join(lst))
    