N = list(input().upper())       # 모두 대문자로 변환

number = [0] * 26               # 문자가 저장될 빈 배열 생성

for i in range(len(N)):         # 해당 인덱스에 문자열 갯수 저장
    ndx = ord(N[i]) - ord('A')
    number[ndx] += 1

max_ = max(number)              # 최댓값 구하기
cnt = 0
index = 0

for i in range(len(number)):
    if max_ == number[i]:       # max_의 인덱스 값 구하기
        index = i
        cnt += 1                # max_의 갯수 확인
    else:
        continue

if cnt == 1:                    # max_가 중복 아닐 때
    print(chr(index + ord("A")))
elif len(N) == 1:               # 문자열이 한 자릿수일 때
    print(N)
else:                           # max_가 중복일 경우
    print('?')
