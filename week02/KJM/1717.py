import sys
sys.stdin = open('week02/KJM/input.txt','r')

'''
0번을 입력받으면 union 함수를 통해 두 요소를 합침
-> union 함수에서 두 요소의 루트노드를 탐색하는데(parent 배열)
두 요소의 루트 노드가 다르면 다른 집합이므로 루트노드를 덮어 씌워 합친다.

만약 루트 노드가 같다면 같은 집합이므로 추가 동작을 하지 않고 끝낸다 


1번을 입력받으면 sameSet 함수를 통해 두 함수가 같은지 체크함 
-> 같은 루트노드를 공유하고 있으면 같은 집합임을 이용  

'''

def findP(get_node):
    if parent[get_node] == -1: # 부모 노드의 정보가 없으면
        return get_node # 본인이 루트노드
    
    # 정보가 있으면 재귀를 통한 깊은 탐색
    res = findP(parent[get_node]) # res변수에 값 저장해놔야 마지막 값 저장
    parent[get_node] = res
    return res 

def union(a,b):
    root_a = findP(a)
    root_b = findP(b)
    
    if root_a == root_b: # 같은 집합이면
        return 
  
    parent[root_b] = root_a # 두개를 같은 그룹으로


def sameSet(a,b):
    return findP(a) == findP(b)


n,m = map(int,input().split())
parent = [-1] * (n+1)

for _ in range(m):
    order, a, b = map(int,input().split())
    if order == 0:
        union(a,b)
    else:
        if sameSet(a,b):
            print('YES')
        else:
            print('NO')