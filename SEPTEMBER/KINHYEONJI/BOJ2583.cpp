#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
    int m, n, k;
    cin >> m >> n >> k;
    vector<vector<int>> v(m, vector<int>(n, 0));
    for (int i = 0; i < k; i++) {
        int x1, y1, x2, y2;
        cin >> y1 >> x1 >> y2 >> x2;
        for (int j = 0; j < x2 - x1; j++) {
            for (int k = 0; k < y2 - y1; k++) {
                v[x1 + j][y1 + k] = -1;
            }
        }
    }
    int dx[] = {-1, 1, 0, 0};
    int dy[] = {0, 0, -1, 1};
    vector<int> answer;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (v[i][j] == 0) {
                v[i][j]=-1;
                queue<pair<int, int>> q;
                int width = 1;
                q.push({i, j});
                while (!q.empty()) {
                    auto cur = q.front();
                    q.pop();
                    for (int dir = 0; dir < 4; dir++) {
                        int nx = cur.first + dx[dir];
                        int ny = cur.second + dy[dir];
                        if (nx < 0 || ny < 0 || nx >= m || ny >= n)continue;
                        if (v[nx][ny] == 0) {
                            v[nx][ny] = -1;
                            width++;
                            q.push({nx, ny});
                        }
                    }
                }
                answer.push_back(width);
            }
        }
    }
    cout << answer.size() << '\n';
    sort(answer.begin(), answer.end());
    for (int i = 0; i < answer.size(); i++) {
        cout << answer[i] << " ";
    }
}