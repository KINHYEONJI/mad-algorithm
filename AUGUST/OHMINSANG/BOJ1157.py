"""
가장 많이 사용된 알파벳, 대소문자 구분X
문자열을 대문자로 변환 --> 리스트에 담기 --> ord 변환 후 '-65'(계산 편의 및 메모리 사용을 줄이기 위해)
버킷에 넣고 맥스값 찾아서 인덱스랑 같이 저장, 해당 인덱스 값 0으로 바꾸고, 다시 맥스 값 출력
맥스값이 이전과 동일하면 '?' 출력, 낮으면 처음 맥스값 출력된 인덱스 번호에 +65 하고 char 바꾸고 출력
"""
# 문자 입력 후 리스트로 변경 및 아스키 코드로 변환
word = input()
word = word.upper()
lst = list(word)
ord_lst = []
for i in lst:
    ord_lst.append(ord(i))


# 버킷 생성 후 아스키코드에 -65 하고 버킷 인덱스에 + 1
# 위 과정으로 알파벳 등장 최빈수 카운트
# 최빈수 찾고, 최빈수의 해당 인덱스 번호 저장
bucket = [0] * 30
for j in ord_lst:
    j -= 65
    bucket[j] += 1
Max_1 = max(bucket)
Max_pt_1 = bucket.index(max(bucket))


# 최빈수의 인덱스 값 0으로 초기화
bucket[Max_pt_1] = 0


# 두 번째 최빈수 찾고, 최빈수의 해당 인덱스 번호 저장
Max_2 = max(bucket)
Max_pt_2 = bucket.index(max(bucket))


# 첫 번째 최빈수와 두 번째 최빈수 비교해서 첫 번째가 더 크면 해당 인덱스 번호에 +65하고 char 형변환 후 출력
# 다르면 '?' 출력
if Max_1 > Max_2:
    print(chr(Max_pt_1 + 65))
else:
    print('?')
