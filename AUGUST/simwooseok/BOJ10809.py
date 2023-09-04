S = list(input())
st = []
for i in S:
    st.append(ord(i)-97)

Bucket = [-1] * 26
for i in range(len(st)):
    Bucket[st[i]] =  st.index(st[i])
print(*Bucket)
