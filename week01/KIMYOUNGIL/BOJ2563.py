n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

squares_sum = 10*10*n

new = []
for i in range(n-1):
    for j in range(n-1,i,-1):
        x_minus = abs(arr[i][0] - arr[j][0])
        y_minus = abs(arr[i][1] - arr[j][1])

        if (x_minus < 10) and (y_minus < 10):
            new.append(arr[i],arr[j])
            # min_x, max_x = min(arr[i][0], arr[j][0]), max(arr[i][0], arr[j][0])
            # min_y, max_y = min(arr[i][1], arr[j][1]), max(arr[i][1], arr[j][1])

            # square_row = (min_x + 10) - (max_x)
            # square_col = (min_y + 10) - (max_y)
            
            # squares_sum -= square_row * square_col

print(new)