s = list(input())
for i in range(ord('a'),ord('z')+1):
    if chr(i) in s:
        print(s.index(chr(i)), end = " ")
    else:
        print(-1, end = " ")