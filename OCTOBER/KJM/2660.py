import sys
sys.stdin = open('input.txt','r')



k = int(input())
nodes = list(map(int,input().split()))
graph =  [ [] for _ in range(k) ]


def binary_separatioin(nodes,depth):
    if len(nodes) == 1:
        graph[depth].extend(nodes)
        return

    mid = len(nodes) // 2
    graph[depth].append(nodes[mid])
    binary_separatioin(nodes[:mid], depth + 1)
    binary_separatioin(nodes[mid + 1:], depth + 1)


binary_separatioin(nodes,0)

for i in range(k):
    if i==0:
        print(graph[i][0])
    else:
        print(*graph[i])