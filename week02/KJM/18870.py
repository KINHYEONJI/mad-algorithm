from bisect import bisect_left

N = int(input())
arr = list(map(int,input().split()))


# 중복을 제거한 후 정렬
sorted_arr = sorted(set(arr))

# 원래 배열의 각 원소에 대해 정렬된 배열에서의 인덱스를 찾아서 그 인덱스로 대체
compressed_arr = []
for val in arr:
    compressed_val = bisect_left(sorted_arr, val)  # 이진 검색을 사용해 인덱스 찾기
    compressed_arr.append(compressed_val)

# 출력
print(*compressed_arr)