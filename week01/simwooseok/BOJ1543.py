st = input()
word = input()
a = 0
cnt = 0
while a < len(st):
    if st[a:].find(word) == -1:
        break
    a += st[a:].find(word) + len(word)
    cnt += 1

print(cnt)