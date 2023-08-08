# 문장을 리스트의 형태로 바꿔서 받고 대문자로 변경
# 대문자 A와 아스키 코드 값을 빼줘서 num 리스트의 값들에 1을 더해주기(bucket의 원리와 동일)
# 출력
st = list(input().upper())
num = [0] *26
for i in range(len(st)):
    ord_st = ord(st[i])
    num[ord(st[i])-ord('A')] +=1
if num.count(max(num)) >=2:
    print('?')
else:
    Index = num.index(max(num))
    print(chr(ord('A')+Index))