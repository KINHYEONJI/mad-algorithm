import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
lst = list(map(int, input().split()))

lst_1 = []
set_lst = set(lst)
for i in set_lst:
    lst_1.append(i)
lst_1.sort()

dict = {}
"""
중복 제거된 lst_1 길이만큼 순회하고, 딕셔너리의  lst_1[i] 키에 i 값을 할당
[-10, -9, 2, 4]
-->
{-10: 0, -9: 1, 2: 2, 4: 3}
"""
print(lst_1)
for i in range(len(lst_1)):
    dict[lst_1[i]] = i

print(dict)

for i in lst:
    print(dict[i], end=' ')
