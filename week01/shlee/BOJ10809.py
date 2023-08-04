# 접근
# 알파벳 개수만큼의 길이를 가지고 -1로 이루어진 리스트 생성
# 입력받은 문자열의 원소의 index를 새로운 리스트의 원소로 대체

st = input()

lst = [-1] * 26
for char in st:
    idx = ord(char) - ord('a')
    lst[idx] = st.index(char)

print(*lst)
