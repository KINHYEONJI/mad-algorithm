# 대문자 변환 
st = list(input())
for i in range(len(st)):
    if st[i].islower():
        st[i] = st[i].upper()

# 입력받은 문자의 갯수를 담은 DAT생성 
bucket = {}
for s in st:
    bucket[s] = bucket.get(s,0) + 1

max_v = -21e8
max_key = 0
for key, value in bucket.items():
    if value > max_v:
        max_v = value
        max_key = key
    
    elif value == max_v:
        max_key = '?'

print(max_key)



# # 1. 입력 받은 문자를 모두 대문자로 변환
# st = list(input())
# for i in range(len(st)):
#     if st[i].islower():
#         st[i] = st[i].upper()

# # 2. A~Z까지 순회하면서 입력받은 문자열에서 가장 많은 갯수를 저장
# max_v = -21e8
# for i in range(ord('A'),ord('Z')+1):
#     if st.count(chr(i)) > max_v: 
#         max_v = st.count(chr(i)) 
        
# # 3. 갯수가 같을 경우 처리를 위해 임시 리스트 생성 
# tmp = []
# for i in st: # 입력받은 문자를 순회 
#     if st.count(i) == max_v: # 문자의 개수가 가장 많은 것들을
#         tmp.append(i) # tmp 리스트에 저장 
        
# # 4. 최대갯수가 2개 이상인 경우와 나머지 나눠서 출력
# tmp = set(tmp) # 중복제거
# if len(tmp) >= 2: # 가장 많은 갯수의 문자가 여러개면
#     print('?') 
# else: 
#     print(*tmp) # 아니면 가장 많은 갯수의 문자열이 들어가있는 tmp리스트 출력