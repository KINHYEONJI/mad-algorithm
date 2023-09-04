S = list(input())
ord_S = []
for i in S:
    ord_S.append(ord(i)-97)
bucket = [-1] * 26
for i in range(len(ord_S)):
    """
    ord_S의 i번 째 인덱스의 값을 버킷의 인덱스 번호 지정하고 아래 값을 할당
    ord_S.index(ord_S[i])는 ord_S의 i번째 인덱스에 들어있는 값
    """
    bucket[ord_S[i]] = ord_S.index(ord_S[i])
print(*bucket)