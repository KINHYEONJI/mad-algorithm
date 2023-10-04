def combi(lev, start):
    if lev == L:
        cntv, cntc = 0, 0
        for i in path:
            if i in vowels:
                cntv += 1
            else:
                cntc += 1
        if cntv >= 1 and cntc >= 2:
            print(*path, sep='')
        return

    for i in range(start, C):
        path[lev] = lst[i]
        combi(lev + 1, i + 1)


L, C = map(int, input().split())
lst = list(input().split())
lst.sort()
vowels = ['a', 'e', 'i', 'o', 'u']
path = [''] * L
combi(0, 0)
