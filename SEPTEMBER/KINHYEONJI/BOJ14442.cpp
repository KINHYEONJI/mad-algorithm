#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <string>

using namespace std;

struct s {
    int x;
    int y;
    int break_cnt;
};

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int main() {
    int n, m, k;
    cin >> n >> m >> k;
    vector<vector<int>> v(n, vector<int>(m));
    vector<vector<vector<int>>> visited(n, vector<vector<int>>(m, vector<int>(k + 1)));
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < m; j++) {
            v[i][j] = s[j] - '0';
        }
    }
    queue<s> q;
    q.push({0, 0, 0});
    visited[0][0][0] = 1;
    while (!q.empty()) {
        auto cur = q.front();
        q.pop();
        for (int dir = 0; dir < 4; dir++) {
            int nx = cur.x + dx[dir];
            int ny = cur.y + dy[dir];
            if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
            if (v[nx][ny] == 1) {
                if (visited[nx][ny][cur.break_cnt + 1]) continue;
                int now_break_cnt = cur.break_cnt + 1;
                if (now_break_cnt > k) continue;
                visited[nx][ny][now_break_cnt] = visited[cur.x][cur.y][cur.break_cnt] + 1;
                q.push({nx, ny, now_break_cnt});
            } else {
                if (visited[nx][ny][cur.break_cnt]) continue;
                visited[nx][ny][cur.break_cnt] = visited[cur.x][cur.y][cur.break_cnt] + 1;
                q.push({nx, ny, cur.break_cnt});
            }
        }
    }
    int min_cnt = 21e8;
    for (int i = 0; i < k + 1; i++) {
        if (visited[n - 1][m - 1][i] == 0) continue;
        min_cnt = min(min_cnt, visited[n - 1][m - 1][i]);
    }
    if (min_cnt == 21e8) cout << -1;
    else cout << min_cnt;
}