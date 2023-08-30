#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Point {
    int x;
    int y;
    int z;
};
vector<vector<vector<char>>> board(30, vector<vector<char>>(30, vector<char>(30, '.')));
vector<vector<vector<int>>> visited(30, vector<vector<int>>(30, vector<int>(30, 0)));
int l, r, c;
int dx[] = {0, 0, 1, -1, 0, 0};
int dy[] = {-1, 1, 0, 0, 0, 0};
int dz[] = {0, 0, 0, 0, 1, -1};


int main() {
    while (true) {
        cin >> l >> r >> c;
        if (l == 0 && r == 0 && c == 0)break;
        queue<Point> q;
        Point E;
        for (int i = 0; i < l; i++) {
            for (int j = 0; j < r; j++) {
                for (int k = 0; k < c; k++) {
                    cin >> board[i][j][k];
                    visited[i][j][k] = 0;
                    if (board[i][j][k] == 'S') {
                        visited[i][j][k] = 1;
                        q.push({j, k, i});
                    }
                    if(board[i][j][k] == 'E'){
                        E = {j, k, i};
                    }
                }
            }
        }
        int answer = 0;
        while (!q.empty()) {
            auto cur = q.front();
            q.pop();
            if (board[cur.z][cur.x][cur.y] == 'E') {
                answer = visited[E.z][E.x][E.y] - 1;
                break;
            }
            for (int dir = 0; dir < 6; dir++) {
                int nx = cur.x + dx[dir];
                int ny = cur.y + dy[dir];
                int nz = cur.z + dz[dir];
                if (nx < 0 || ny < 0 || nz < 0 || nx >= r || ny >= c || nz >= l) continue;
                if (board[nz][nx][ny] == '#') continue;
                if(visited[nz][nx][ny]) continue;
                visited[nz][nx][ny] = visited[cur.z][cur.x][cur.y] + 1;
                q.push({nx, ny, nz});
            }
        }

        if (answer==0) cout << "Trapped!" << '\n';
        else cout << "Escaped in " << answer << " minute(s)." << '\n';
    }
}