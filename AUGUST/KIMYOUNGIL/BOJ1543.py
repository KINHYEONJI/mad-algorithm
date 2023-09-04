doc = input()
search = input()

if len(doc) > len(search):
    i = 0
    cnt = 0
    while i < len(doc)-len(search)+1:
        if doc[i:i+len(search)] == search:
            cnt += 1
            i += len(search)
        else:
            i += 1
    print(cnt)

elif doc == search:
    print(1)

else:
    print(0)
