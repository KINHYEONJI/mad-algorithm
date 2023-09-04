st = input()
lst = []
for i in range(len(st)):
    if st[i].isupper():         # 대문자
        if ord(st[i]) + 13 > ord('Z'):
            elem = chr((ord('A') + ord(st[i]) - ord('Z') + 12))
        else:
            elem = chr(ord(st[i]) + 13)
    elif st[i].islower():       # 소문자
        if ord(st[i]) + 13 > ord('z'):
            elem = chr((ord('a') + ord(st[i]) - ord('z') + 12))
        else:
            elem = chr(ord(st[i]) + 13)
    else:                       # 알파벳 제외 문자(숫자,공백)
        elem = st[i]

    lst.append(elem)

print(''.join(lst))
