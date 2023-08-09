#include <iostream>
#include <queue>

using namespace std;

#define x first
#define y second
char maze[1000][1000] = {};
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int main() {
    int N, M;
    cin >> N >> M;
    queue<pair<int, int>> q_fire;
    queue<pair<int, int>> q_jh;
    vector<vector<int>> v_fire(N, vector<int>(M, 1000001));
    vector<vector<int>> v_jh(N, vector<int>(M, 1000001));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> maze[i][j];
            if (maze[i][j] == 'F') {
                q_fire.push({i, j});
                v_fire[i][j] = 1;
            }
            if (maze[i][j] == 'J') {
                q_jh.push({i, j});
                v_jh[i][j] = 1;
            }
        }
    }

    while (!q_fire.empty()) {
        auto cur_fire = q_fire.front();
        q_fire.pop();
        for (int dir = 0; dir < 4; dir++) {
            int nx = cur_fire.x + dx[dir];
            int ny = cur_fire.y + dy[dir];
            if (nx < 0 || nx >= N || ny < 0 || ny >= M)continue;
            if (maze[nx][ny] != '#' && v_fire[nx][ny] == 1000001) {
                v_fire[nx][ny] = v_fire[cur_fire.x][cur_fire.y] + 1;
                q_fire.push({nx, ny});
            };
        }
    }
    while (!q_jh.empty()) {
        auto cur_jh = q_jh.front();
        q_jh.pop();
        for (int dir = 0; dir < 4; dir++) {
            int nx = cur_jh.x + dx[dir];
            int ny = cur_jh.y + dy[dir];
            if (nx < 0 || nx >= N || ny < 0 || ny >= M)continue;
            if (maze[nx][ny] != '#' && v_jh[nx][ny] == 1000001) {
                v_jh[nx][ny] = v_jh[cur_jh.x][cur_jh.y] + 1;
                q_jh.push({nx, ny});
            };
        }
    }

    int min_move = 21e8;
    for (int i = 0; i < N; i++) {
        if (maze[i][0] != '#' && v_jh[i][0] != 0 && (v_fire[i][0] > v_jh[i][0])) {
            min_move = min(v_jh[i][0], min_move);
        }
        if (maze[i][M - 1] != '#' && v_jh[i][M - 1] != 0 && (v_fire[i][M - 1] > v_jh[i][M - 1])) {
            min_move = min(v_jh[i][M - 1], min_move);
        }
    }
    for (int i = 1; i < M; i++) {
        if (maze[0][i] != '#' && v_jh[0][i] != 0 && (v_fire[0][i] > v_jh[0][i])) {
            min_move = min(v_jh[0][i], min_move);
        }
        if (maze[N - 1][i] != '#' && v_jh[N - 1][i] != 0 && (v_fire[N - 1][i] > v_jh[N - 1][i])) {
            min_move = min(v_jh[N - 1][i], min_move);
        }
    }
    if (min_move == 21e8) cout << "IMPOSSIBLE";
    else cout << min_move;
}

