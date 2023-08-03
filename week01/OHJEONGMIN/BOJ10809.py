st = input()
lst = [0]*26
alpha = ord('a')
for i in range(26):
    Index = 0
    if chr(alpha) in st:
        Index = st.index(chr(alpha))
        lst[i] = Index
    else:
        lst[i] = -1
    alpha+=1
print(*lst)
