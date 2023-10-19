#include <iostream>
#include <queue>
#include <vector>
#include <tuple>
using namespace std;
int n, m;
int b[102][102];
int d[102][102];
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int main() {
    cin >> m >> n;
    for (int i = 1; i <= n; i++) {
        string str;
        cin >> str;
        for (int j = 1; j <= m; j++) {
            b[i][j] = str[j - 1] - '0';
        }
    }

    for (int i = 0; i <= n; i++) {
        fill(d[i] + 1, d[i] + m + 1, 0x3f3f3f3f);
    }

    priority_queue<tuple<int, int, int>,
            vector<tuple<int, int, int>>,
            greater<tuple<int, int, int>>> pq;

    d[1][1] = 0;
    pq.push({0, 1, 1});
    while (!pq.empty()) {
        int cw, cx, cy;
        tie(cw, cx, cy) = pq.top();
        pq.pop();
        if (d[cx][cy] != cw) continue;

        for (int dir = 0; dir < 4; dir++) {
            int nx = cx + dx[dir];
            int ny = cy + dy[dir];
            if (nx > n || nx < 1) continue;
            if (ny > m || ny < 1) continue;
            int nw = cw + b[nx][ny];
            if (nw < d[nx][ny]) {
                d[nx][ny] = nw;
                pq.push({nw, nx, ny});
            }
        }
    }
    cout<<d[n][m];
}