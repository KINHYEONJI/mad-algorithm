str=input()
b=list(str.upper()) #대문자로 다 바꾼다
c=list(set(b)) #문자 검사 set으로 중복제거 #셋에는 순서가 없으니 리스트를 씌어서 사용

a=[]

max=0
ic=0#인덱스 카운트용 나중에 문자값다시 뱉을 때 사용
for i in c: #문자로 max값을 찾는다
    a.append(b.count(i))

    if max<b.count(i):
        max=b.count(i)
        index=ic #  max 인덱스를 구해둔다
    ic+=1    
ct=0

for i in a: #max값이 여러개이면 카운트 늘린다
    if i == max:
        ct+=1


if ct<=1: #카운트 개수에 따라 답변 출력
    print(c[index])
else:
    print('?')