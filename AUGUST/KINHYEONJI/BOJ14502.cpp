#include <iostream>
#include <queue>

using namespace std;

#define x first
#define y second

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
int lab[8][8];
int copy_lab[8][8];
int n, m;
int max_safe = 0;
queue<pair<int, int>> q;
queue<pair<int, int>> copy_q;

void copyq() {
    for (int i = 0; i < q.size(); i++) {
        auto cur = q.front();
        copy_q.push(cur);
        q.pop();
        q.push(cur);
    }
}

void virus() {
    copy_lab[8][8];
    copyq(); //원본 배열은 그대로 두고 깊은 복사로 만든 새로운 배열에서 bfs 진행
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            copy_lab[i][j] = lab[i][j];
        }
    }

    while (!copy_q.empty()) {
        auto cur = copy_q.front();
        copy_q.pop();
        for (int dir = 0; dir < 4; dir++) {
            int nx = cur.x + dx[dir];
            int ny = cur.y + dy[dir];
            if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
            if (copy_lab[nx][ny] == 0) {
                copy_lab[nx][ny] = 2;
                copy_q.push({nx, ny});
            }
        }
    }
}

void check_arr() {
    int safe_cnt = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (!copy_lab[i][j]) safe_cnt++;
        }
    }
    max_safe = max(max_safe, safe_cnt);
}

void dfs(int level, int s) {
    if (level == 3) { //벽을 3개다 지었을 경우 바이러스를 퍼뜨리고 안전한 지역을 찾음
        virus();
        check_arr();
        return;
    }

    for (int i = s; i < n * m ; i++) {
        int x = i / m;
        int y = i % m;
        if (lab[x][y] == 0) {
            lab[x][y] = 1;
            dfs(level + 1, i + 1);
            lab[x][y] = 0;
        }
    }
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> lab[i][j];
            if (lab[i][j] == 2) {
                q.push({i, j});
            }
        }
    }

    dfs(0, 0); //벽을 세울 3개의 좌표를 찾음
    cout << max_safe;
    return 0;
}

