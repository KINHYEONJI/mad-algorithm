#include <iostream>
#include <queue>
#include <string>

using namespace std;

#define x first
#define y second

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
int maze[102][102] = {};
int count[102][102] = {};


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N, M;
    cin >> N >> M;

    for (int i = 0; i < N; i++) {
        string str;
        cin >> str;
        for (int j = 0; j < M; j++) {
            maze[i][j] = str[j] - '0';
        }
    }

    queue<pair<int, int>> q;
    count[0][0] = 1;
    q.push({0, 0});
    while (!q.empty()) {
        auto cur = q.front();
        q.pop();
        for (int dir = 0; dir < 4; dir++) {
            int nx = cur.x + dx[dir];
            int ny = cur.y + dy[dir];
            if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
            if (count[nx][ny] || !maze[nx][ny]) continue;
            count[nx][ny] = count[cur.x][cur.y] + 1;
            q.push({nx, ny});
        }
    }
    cout << count[N - 1][M - 1];
}