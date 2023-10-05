#include <iostream>
#include <vector>
#include <queue>

using namespace std;

#define X first
#define Y second
int dx[4] = {0, -1, 0, 1};
int dy[4] = {1, 0 , -1, 0};
vector<pair<int, int> > player[10];
int res[10];
int s[10];
char board[1000][1000];
int n, m, p;

void bfs() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (board[i][j] != '.' && board[i][j] != '#') {
                player[board[i][j] - '0'].push_back({ i, j });
            }
        }
    }
    queue< pair<int, int > > Q[10];
    for (int i = 1; i <= p; i++) {
        for (auto castle : player[i]) {
            Q[i].push({ castle.X, castle.Y });
            res[i]++;
        }
    }

    while (true) { //라운드 시작
        bool success = false;
        for (int i = 1; i <= p; i++) { //1번 플레이부터 시작
            int s_len = s[i]; //i번 플레이어의 최대 이동 횟수
            while (!Q[i].empty() && s_len--) { // i번 플레이어 BFS
                int Q_size = Q[i].size();
                for(int j=0; j<Q_size; j++){
                    auto cur = Q[i].front(); Q[i].pop();
                    for (int dir = 0; dir < 4; dir++) {
                        int nx = cur.X + dx[dir];
                        int ny = cur.Y + dy[dir];
                        if (nx < 0 || ny < 0 || nx >= n || ny >= m)continue;
                        if (board[nx][ny] == '.') { // 성을 건설할 수 있으면
                            Q[i].push({ nx, ny });
                            board[nx][ny] = board[cur.X][cur.Y];
                            res[i]++;
                            success = true;
                        }
                    }
                }
            }

        }
        if (!success) break;
    }
}

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m >> p;
    for (int i = 1; i <= p; i++) {
        cin >> s[i];
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> board[i][j];
        }
    }
    bfs();

    for (int i = 1; i <= p; i++) {
        cout << res[i] << ' ';
    }

    return 0;
}