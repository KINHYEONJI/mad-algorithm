"""
n이 몇 번째 껍질(orbitral)에 위치해 있는지
N = 1, orbital = 1
+6
n = 7, orbital = 2
+12
n = 19, orbital = 3
+18
n = 37, orbital = 4
+24
n = 61, orbital = 5
6의 배수만큼 증가
"""
N = int(input())
orbital = 1
room = 1
while N > room:
    # orbital이 증가하는 조건. 초기값 1, 7, 19,... 일때 6의 배수만큼 곱해야 다름 orbital로 넘어감
    room = 6 * orbital + room
    orbital += 1
print(orbital)
