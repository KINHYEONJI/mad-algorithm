#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    int arr[102][102] = {};
    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        for (int j = a; j < a + 10; j++) {
            for (int k = b; k < b + 10; k++) {
                arr[j][k] = 1;
            }
        }
    }
    int length = 0;
    int dx[] = {-1, 1, 0, 0};
    int dy[] = {0, 0, -1, 1};
    for (int i = 1; i < 102; i++) {
        for (int j = 1; j < 102; j++) {
            if (arr[i][j]==1) {
                for (int k = 0; k < 4; k++) {
                    int nx = i + dx[k];
                    int ny = j + dy[k];
                    if (arr[nx][ny] == 0) length++;
                }
            }
        }
    }
    cout << length;
}
