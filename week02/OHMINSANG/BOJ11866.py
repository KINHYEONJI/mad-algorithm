"""
요세푸스 문제()
0부터 len(n)까지, for 문 돌려서 k-1스탭씩 가서 버리고, i > len(k)일 때는 나눠서 나머지의 인덱스 번호에 해당 값 제거
"""
n, k = map(int, input().split())
lst = []
for j in range(1, n + 1):
    lst.append(j)
k = k - 1
lstt = []

while len(lst) > 0:
    k = k % len(lst)
    x = lst.pop(k)
    lstt.append(x)
    k += 2
    if k >= len(lst):
        k -= 1


print(f'<{", ".join(map(str, lstt))}>')
