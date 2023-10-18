# 부모가 처음 배열값인 -1이면 그대로 return
# 다르면 최상위 부모를 return
def find(num):
    global parent
    if parent[num] == -1:
        return num
    
    result = find(parent[num])
    parent[num] = result
    return result

# 두 수를 find함수로 보내 최상위 부모를 return받아
# 연결시켜준다

def union(n1, n2):
    global parent
    f_num1, f_num2 = find(n1), find(n2)

    if f_num1 == f_num2:
        return
    else:
        parent[f_num2] = f_num1

N, M = map(int, input().split())
parent = [-1] * (N+1)
for i in range(M):
    first, n1, n2 = map(int, input().split())


    if first == 0:
        union(n1, n2)
    
    else:
        if find(n1) == find(n2):
            print('YES')
        else:
            print('NO')
