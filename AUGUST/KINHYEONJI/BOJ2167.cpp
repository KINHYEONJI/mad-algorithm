#include <iostream>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    int arr[N][M];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> arr[i][j];
        }
    }
    int count;
    cin >> count;
    while (count--) {
        int i, j, x, y;
        cin >> i >> j >> x >> y;
        int sum = 0;
        for (int row = i - 1; row < x; row++) {
            for (int col = j - 1; col < y; col++) {
                sum += arr[row][col];
            }
        }

        cout << sum << '\n';
    }
}