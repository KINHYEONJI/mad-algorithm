#include <iostream>
#include <vector>
#include <queue>

#define x first
#define y second

using namespace std;

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int main() {
    int n;
    cin >> n;
    vector<vector<int>> map(100, vector<int>(100, 0));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> map[i][j];
        }
    }
    int cnt = 1;
    vector<vector<int>> visited(100, vector<int>(100, 0));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (!map[i][j])continue;
            if (visited[i][j])continue;
            queue<pair<int, int>> q;
            q.push({i, j});
            map[i][j] = cnt;
            visited[i][j] = 1;
            while (!q.empty()) {
                auto cur = q.front();
                q.pop();
                for (int dir = 0; dir < 4; dir++) {
                    int nx = cur.x + dx[dir];
                    int ny = cur.y + dy[dir];
                    if (nx < 0 || ny < 0 || nx >= n || ny >= n) continue;
                    if (!map[nx][ny]) continue;
                    if (visited[nx][ny]) continue;
                    map[nx][ny] = cnt;
                    visited[nx][ny] = 1;
                    q.push({nx, ny});
                }
            }
            cnt++;
        }
    }
    int answer = 21e8;
    int island_num = 1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (map[i][j] != island_num) continue;
            queue<pair<int, int>> q;
            vector<vector<int>> bridge_cnt(100, vector<int>(100, 0));
            q.push({i, j});
            bridge_cnt[i][j] = 1;
            while (!q.empty()) {
                auto cur = q.front();
                q.pop();
                for (int dir = 0; dir < 4; dir++) {
                    int nx = cur.x + dx[dir];
                    int ny = cur.y + dy[dir];
                    if (nx < 0 || ny < 0 || nx >= n || ny >= n) continue;

                    //바다를 만날 경우
                    if (!map[nx][ny]) {
                        //이미 지어진 다리가 있을 경우
                        if (bridge_cnt[nx][ny]) {
                            // 이미 지어진 다리가 더 짧을 경우 무시하고 진행
                            if (bridge_cnt[nx][ny] <= bridge_cnt[cur.x][cur.y] + 1) continue;
                        }
                        bridge_cnt[nx][ny] = bridge_cnt[cur.x][cur.y] + 1;
                        q.push({nx, ny});
                    }
                    //본인 섬을 만날 경우
                    else if (map[nx][ny] == island_num) {
                        if(!map[cur.x][cur.y]) continue;
                        if(bridge_cnt[nx][ny]) continue;
                        bridge_cnt[nx][ny] = bridge_cnt[cur.x][cur.y];
                        q.push({nx, ny});
                    }
                    //다른 섬을 만난 경우
                    else {
                        answer = min(answer, bridge_cnt[cur.x][cur.y] - 1);
                    }
                }
            }
            island_num++;
        }
    }
    cout << answer;
}