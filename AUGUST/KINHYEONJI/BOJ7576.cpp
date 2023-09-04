#include <iostream>
#include <queue>

using namespace std;

#define x first
#define y second

int box[1002][1002] = {};
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int main() {
    int N, M;
    cin >> N >> M;
    queue<pair<int, int>> q;
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            cin >> box[i][j];
            if (box[i][j] == 1) q.push({i, j});
        }
    }

    while (!q.empty()) {
        auto cur = q.front();
        q.pop();
        for (int dir = 0; dir < 4; dir++) {
            int nx = cur.x + dx[dir];
            int ny = cur.y + dy[dir];

            if (nx < 0 || nx >= M || ny < 0 || ny >= N) continue;
            if (box[nx][ny] == -1 || box[nx][ny]) continue;
            box[nx][ny] = box[cur.x][cur.y] + 1;
            q.push({nx, ny});
        }
    }
    int day = 0;
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            if (box[i][j] == 0) {
                cout << -1;
                return 0;
            }
            if (box[i][j] > day) day = box[i][j];
        }
    }
    cout << day - 1;

}