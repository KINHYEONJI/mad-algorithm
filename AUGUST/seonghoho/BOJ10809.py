S = list(input())
English = [-1]*26 # 알파벳 갯수만큼 -1 바구니 생성

for i in range(len(S)): # 입력 단어의 자릿수만큼 반복
    num = ord(S[i])-ord('a') #입력 단어의 i번째 문자의 수
    if English[num] == -1: #중복이 아니면 실행
        English[num] = i # 바구니의 알파벳 순서에 문자 위치 입력
    else:
        continue

for i in range(len(English)):
    print(English[i], end=' ')
