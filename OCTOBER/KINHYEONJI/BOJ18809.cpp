#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

struct st {
    int x;
    int y;
    int color;
};
using namespace std;

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int main() {
    int n, m, g, r;
    cin >> n >> m >> g >> r;
    int garden[50][50];
    int can_gr = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> garden[i][j];
            if (garden[i][j] == 2) can_gr++;
        }
    }
    can_gr -= (g + r);
    vector<int> for_combination;
    while (can_gr--) {
        for_combination.push_back(0);
    }
    while (g--) {
        for_combination.push_back(1);
    }
    while (r--) {
        for_combination.push_back(2);
    }

    int max_cnt = 0;
    do {
        int cnt = 0;
        int visited[50][50][3] = {0};
        int index = 0;
        queue<st> g_q;
        queue<st> r_q;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (garden[i][j] == 2) {
                    visited[i][j][for_combination[index]] = 1;
                    if (for_combination[index] == 1) {
                        g_q.push({i, j, 1});
                        visited[i][j][1] = 1;
                    } else if (for_combination[index] == 2) {
                        r_q.push({i, j, 2});
                        visited[i][j][2] = 1;
                    }
                    index++;
                }
            }
        }

        while (!r_q.empty()) {
            g_q.push(r_q.front());
            r_q.pop();
        }

        while (!g_q.empty()) {
            auto cur = g_q.front();
            g_q.pop();
            if (visited[cur.x][cur.y][0] == -1) continue;
            for (int dir = 0; dir < 4; dir++) {
                int nx = cur.x + dx[dir];
                int ny = cur.y + dy[dir];
                if (nx < 0 || ny < 0 || nx >= n || ny >= m)continue;
                if (garden[nx][ny] == 0) continue;
                if (visited[nx][ny][cur.color]) continue;
                visited[nx][ny][cur.color] = visited[cur.x][cur.y][cur.color] + 1;
                g_q.push({nx, ny, cur.color});
                if (visited[nx][ny][1] == visited[nx][ny][2]) {
                    cnt++;
                    visited[nx][ny][0] = -1;
                }
            }
        }
        max_cnt = max(max_cnt, cnt);
    } while (next_permutation(for_combination.begin(), for_combination.end()));
    cout << max_cnt;
}