"""

재귀 함수를 활용하여 중복 순열의 모든 가능한 값을 생성하고, 새로운 리스트에 추가하여
그 중 n 이하의 최댓값을 찾는 방법으로 접근.

이때, n의 자릿수에 따라 사용하는 리스트의 길이가 달라져야함에 주의해야하고
이를 방지하기 위해 입력받는 배열(arr)에 0을 원소로 추가한다.

ex) n=100, k=3, arr= [1,5,7] 이 입력되면
세 자리수인 n에 따라 path의 길이를 3으로 만들고 arr에 0을 추가한 후,
최댓값을 우선 077로 만들고 마지막에 0울 제거하여 77로 만들 예정.

"""



n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.append(0)             # 배열에 0을 원소로 추가

num = len(str(n))       # n의 자릿수 구하기 -> path 배열의 크기를 결정해야함.

path = [''] * num       # n의 자릿수만큼 배열 생성
lst = []                # 중복 순열의 값들을 추가할 리스트 생성


def abc(lev):                       # 중복 순열 모든 값들을 구하는 재귀함수 생성

    if lev == num:
        value = ''.join(map(str, path))     # path는 정수들을 원소로 가지므로, 문자열로 바꾼뒤 join울 아용하여 출력
        lst.append(value)               # 중복 순열 값들을 리스트에 추가
        return

    for i in range(len(arr)):    # len(arr)==k+1 이어도 상관 없음.
        path[lev] = arr[i]
        abc(lev + 1)


abc(0)              # 재귀 호출


newlst = []
for s in lst:
    new_s = s.replace('0', '')          # 임의로 추가했던 0을 ''(빈 문자열) 로 바꾸고,
    if new_s != '':                     # 문자열을 원소로 갖는 lst를 정수형으로 바꿈.
        newlst.append(int(new_s))       # 이떄, 빈 문자열은 정수형으로 고칠 수 없으므로 제외함.


final_lst = [x for x in newlst if x <= n]     # n 이하의 정수만 모은 최종 리스트 생성

print(max(final_lst))

