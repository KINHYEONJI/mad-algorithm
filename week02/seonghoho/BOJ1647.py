def bossfind(a):
    global arr
    if arr[a]==0:   # a에게 보스가 없다면 return 하기
        return a
    ret = bossfind(arr[a])      # 보스가 있다면 그 보스의 보스가 있는지 재귀로 확인
    arr[a] = ret    # 해당 문자의 보스를 최종 보스로 덮어 씌워서 다음 번에 빨리 접근하게 만들기
    return ret      # return 받은 최종 보스 a값을 끝까지 가지고 나오기

def union(x, y, i):
    global total, arr, cnt  # 해당 길의 boss를 찾는 함수의 값을 변수에 지정
    bossx, bossy = bossfind(x), bossfind(y)
    if bossx == bossy:  # 두 길의 보스가 같다면 cycle이 생기니 return
        return
    total += lst[i][2]  # 보스가 같지 않은 두 길의 유지비 더하기
    cnt+= 1     # 연결된 길의 갯수 하나 더하기
    arr[bossy] = bossx  # 비어있는 bossy의 보스를 bossx로 할당하기

total = 0
cnt = 0

N, M = map(int, input().split())    # 집의 개수 N, 길의 개수 M
lst = [list(map(int, input().split())) for _ in range(M)]
lst.sort(key=lambda x: x[2])    # 길의 유지비 기준으로 sort
arr = [0] * (N + 1)  # 집의 개수 보다 하나 더 만들기

for i in range(M):
    if cnt == N-2:  # 두 마을로 나눴으니 필요한 길의 갯수는 N-2
        print(total)    # 총 유지비 출력
        break
    union(lst[i][0], lst[i][1], i)  # 연결된 두 집과 비용 union에 넣기