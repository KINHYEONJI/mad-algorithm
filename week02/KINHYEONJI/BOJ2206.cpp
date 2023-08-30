#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>

using namespace std;

struct Point {
    int break_cnt;
    int x;
    int y;
};
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
vector<vector<int>> map(1000, vector<int>(1000, 0));
vector<vector<pair<int, int>>> visited(1000, vector<pair<int, int>>(1000, {0, 0}));
//first 벽을 이미 부시고 방문
//second 길로만 방문

int main() {
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        string str;
        cin >> str;
        for (int j = 0; j < m; j++) {
            map[i][j] = str[j] - '0';
        }
    }
    queue<Point> q;
    q.push({0, 0, 0});
    visited[0][0].second = 1;
    while (!q.empty()) {
        auto cur = q.front();
        q.pop();
        if (cur.x == n - 1 && cur.y == m - 1) break;
        for (int dir = 0; dir < 4; dir++) {
            int nx = cur.x + dx[dir];
            int ny = cur.y + dy[dir];
            if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
            //벽을 한번 부순 상태
            if (cur.break_cnt) {
                //다시 벽을 만난 경우
                if (map[nx][ny]) continue;
                    //길을 만난 경우
                else {
                    //이동할 칸에 이미 벽을 부시고 방문한 적 있는 경우
                    if (visited[nx][ny].first) continue;
                    //한번도 벽을 부시고 방문한 적 없는 경우
                    visited[nx][ny].first = visited[cur.x][cur.y].first + 1;
                    q.push({1, nx, ny});
                }

            }
                //벽을 한번도 안 부신 상태
            else {
                //벽을 만난 경우
                if (map[nx][ny]) {
                    //벽을 부시고 방문한 적 있는 경우
                    if (visited[nx][ny].first) continue;
                    //벽을 처음 부시는 경우
                    visited[nx][ny].first = visited[cur.x][cur.y].second + 1;
                    q.push({1, nx, ny});
                }
                    //길을 만난 경우
                else {
                    if (visited[nx][ny].second) continue;
                    visited[nx][ny].second = visited[cur.x][cur.y].second + 1;
                    q.push({0, nx, ny});
                }
            }

        }
    }
    int break_answer = visited[n - 1][m - 1].first;
    int answer = visited[n - 1][m - 1].second;
    if (break_answer && answer) cout << min(break_answer, answer);
    else if (!break_answer && !answer) cout << -1;
    else cout << max(break_answer, answer);
}