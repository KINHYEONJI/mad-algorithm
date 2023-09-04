st = input().split(" ")

rot13 = []
for i in st:

    ord_len = []
    for j in range(len(i)):
        ord_len.append(ord(i[j]))

    word = ""
    for k in ord_len:
        if 97 <= k <= 122:
            if k+13 > ord('z'):
                k -= 26
                word += chr(k+13)
            else:
                word += chr(k+13)
        elif 65 <= k <= 90:
            if k+13 > ord('Z'):
                k -= 26
                word += chr(k+13)
            else:
                word += chr(k+13)
        else:
            word += chr(k)
    rot13.append(word)

print(*rot13, sep =" ")