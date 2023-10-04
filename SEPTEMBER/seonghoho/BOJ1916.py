import heapq
import sys

N = int(sys.stdin.readline())  # 도시 갯수
M = int(sys.stdin.readline())  # 버스 갯수

lst = [[] for _ in range(N + 1)]  # 도시 번호가 1부터 시작하니 N+1개 생성
for i in range(M):  # lst[a] 안에 (b,c) 넣기
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    lst[a].append((b,c))
start, end = map(int, sys.stdin.readline().rstrip().split())  # start, end 입력받기

inf = int(21e8)  # 도시 갯수만큼 result 배열 만들어서 infinity 로 채우기
result = [inf] * (N + 1)


def dijkstra(start):  # 다익스트라 함수 생성
    heap = []  # heap 배열 생성
    heapq.heappush(heap, (0, start))  # k 경유지 들렀을 때의 값이 왼쪽, k 경유지 번호가 오른쪽
    result[start] = 0  # 시작점을 경유지로 둔 상황이기에, 비용은 0

    while heap:  # heap에 원소가 존재하면 실행
        sk, k = heapq.heappop(heap)

        if sk > result[k]: continue  # 경유한 값이 갱신된 결괏값보다 크면 패스

        for i in lst[k]:  # k에서 갈 수 있는 경유지를 lst에 저장해두었으니, 하나씩 꺼내보자
            cost = sk + i[1]  # 현재 경유한 곳의 위치에서 또 경유지 값을 더하면 도착점 비용이다
            if cost < result[i[0]]:  # 경유지 들렀을 때의 비용으로 갱신되면
                result[i[0]] = cost  # result 값 갱신
                heapq.heappush(heap, (cost, i[0]))  # heap에 값 넣기


dijkstra(start)

print(result[end])
