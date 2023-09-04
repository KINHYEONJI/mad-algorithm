words = list(input())                           # 문장 입력받기
new_words = []                                  # 새로 만들어질 문장

for i in words:
    if ord('a') <= ord(i) <= ord('z'):          # 소문자일 경우
        if ord(i) + 13 <= ord('z'):
            new_words.append(chr(ord(i) + 13))
        else:                                   # +13 했을 때 z 넘어갈 경우 -13
            new_words.append(chr(ord(i) - 13))

    elif ord('A') <= ord(i) <= ord('Z'):        # 대문자일 경우
        if ord(i) + 13 <= ord('Z'):
            new_words.append(chr(ord(i) + 13))
        else:                                   # +13 했을 때 z 넘어갈 경우 -13
            new_words.append(chr(ord(i) - 13))

    else:
        new_words.append(i)

print(*new_words, sep='')
