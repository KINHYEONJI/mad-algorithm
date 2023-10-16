from collections import defaultdict, deque
import sys
def input(): return sys.stdin.readline().rstrip()


n = int(input())

# 친구 관계 무방향 딕셔너리로 받기
friendship = defaultdict(list)
while 1:
    person1, person2 = map(int, input().split())
    if person1 == person2 == -1: break
    friendship[person1].append(person2)
    friendship[person2].append(person1)

result = defaultdict(int)

# 딕셔너리 키 순회 할 때마다 bfs 시행. used 초기화
for i in range(1, n + 1):
    used = [0] * (n + 1)
    used[i] = 1
    now = [i, 0]
    q = deque()
    q.append(now)
    while q:
        person, cost = q.popleft()

        # 딕셔너리 키에 밸류 만큼 순회
        for value in friendship[person]:
            if used[value] != 0: continue
            q.append([value, cost + 1])
            used[value] = cost + 1

        # 딕셔너리 특정 키 순회 끝나면 used 최대값을 result[i]에 할당
        # 몇 사람 거치면 모두가 아는 사이라서 0이 나올 수 없음
        result[i] = max(used)

# 이중에 가장 작은 값이 회장 후보 점수
ans = min(result.values())
lst = []

# result 딕셔너리에서 ans와 같은 value 가지는 key값 찾기
for key, value in result.items():
    if value == ans:
        lst.append(key)

# 결과 출력
print(ans, len(lst))
print(*lst)
