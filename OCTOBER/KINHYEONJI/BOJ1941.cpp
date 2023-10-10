#include <iostream>
#include <algorithm>
#include <queue>

#define x first
#define y second

using namespace std;

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
char arr[5][5];
int answer = 0;
bool pos[25];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    for (int i = 0; i < 5; i++) {
        string str;
        cin >> str;
        for (int j = 0; j < 5; j++) {
            arr[i][j] = str[j];
        }
    }

    fill(pos + 18, pos + 25, true);

    do {
        int check[5][5] = {0};
        int visited[5][5] = {0};
        int s_cnt = 0;
        int adj = 1;
        queue<pair<int, int>> q;
        for (int i = 0; i < 25; i++) {
            if (pos[i]) {
                check[i / 5][i % 5] = 1;
                if (q.empty()) {
                    q.push({i / 5, i % 5});
                    visited[i / 5][i % 5] = 1;
                    if (arr[i / 5][i % 5] == 'S') s_cnt++;
                }
            }
        }

        while (!q.empty()) {
            auto cur = q.front();
            q.pop();
            for (int dir = 0; dir < 4; dir++) {
                int nx = cur.x + dx[dir];
                int ny = cur.y + dy[dir];
                if (nx < 0 || ny < 0 || nx >= 5 || ny >= 5)continue;
                if (!check[nx][ny]) continue;
                if (visited[nx][ny]) continue;
                if (arr[nx][ny] == 'S') s_cnt++;
                q.push({nx, ny});
                visited[nx][ny] = 1;
                adj++;
            }
        }
        if (adj == 7 && s_cnt >= 4) answer++;
    } while (next_permutation(pos, pos + 25));
    cout << answer;
}

