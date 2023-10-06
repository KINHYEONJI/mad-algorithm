#include <iostream>
#include <queue>
#include <algorithm>


using namespace std;

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
int n, m, k;
int map[1002][1002];
int visited[1002][1002][12]; //[][][0] -> 벽 여부 , [][][부신벽 개수]
struct st {
    int x;
    int y;
    int is_night;
    int break_cnt;
};

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m >> k;
    for (int i = 1; i <= n; i++) {
        string str;
        cin >> str;
        for (int j = 0; j < m; j++) {
            map[i][j + 1] = str[j] - '0';
        }
    }

    queue<st> q;
    q.push({1, 1, 0, 0});
    visited[1][1][0] = 1;
    while (!q.empty()) {
        auto cur = q.front();
        if (cur.x == n && cur.y == m) break;
        q.pop();
        for (int dir = 0; dir < 4; dir++) { //밤이면 한번 더 있어도 됨. 낮이면 굳이?
            int nx = cur.x + dx[dir];
            int ny = cur.y + dy[dir];
            if (nx < 1 || ny < 1 || nx > n || ny > m) continue;

            if (map[nx][ny]) {
                //밤이라서 벽을 부시지 못하는 경우
                if (cur.is_night) continue;
                //이미 최대로 벽을 다 부셨을
                if (cur.break_cnt == k) continue;
                //이미 그 개수 만큼 벽을 부셔서 방문 한 적 있을 경우
                if (visited[nx][ny][cur.break_cnt + 1]) continue;
                visited[nx][ny][cur.break_cnt + 1] = visited[cur.x][cur.y][cur.break_cnt] + 1;
                q.push({nx, ny, !cur.is_night, cur.break_cnt + 1});
            } else {
                if (visited[nx][ny][cur.break_cnt]) continue;
                visited[nx][ny][cur.break_cnt] = visited[cur.x][cur.y][cur.break_cnt] + 1;
                q.push({nx, ny, !cur.is_night, cur.break_cnt});
            }

        }
        if (cur.is_night) {
            visited[cur.x][cur.y][cur.break_cnt] += 1;
            q.push({cur.x, cur.y, !cur.is_night, cur.break_cnt});
        }
    }


    int answer = 21e8;
    for (int i = 0; i <= k; i++) {
        if (!visited[n][m][i]) continue;
        answer = min(answer, visited[n][m][i]);
    }
    if (answer == 21e8) cout << -1;
    else cout << answer;
}