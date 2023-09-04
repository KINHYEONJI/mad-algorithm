def ROT13(value):
    if 'a' <= value <= 'z':
        if ord(value)+13 <= ord('z'):
            return chr(ord(value)+13)
        elif ord(value)+13 > ord('z'):
            num = ord('z') - ord(value)
            return chr(ord('a')+12-num)
    elif 'A' <= value <= 'Z':
        if ord(value) + 13 <= ord('Z'):
            return chr(ord(value) + 13)
        elif ord(value) + 13 > ord('Z'):
            num = ord('Z') - ord(value)
            return chr(ord('A') + 12-num)
    else:
        return value

st =  input()
for i in range(len(st)):
    ret = ROT13(st[i])
    print(ret,end='')