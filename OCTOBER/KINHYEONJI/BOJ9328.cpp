#include <iostream>
#include <vector>
#include <stack>
#include <queue>

#define X first
#define Y second

using namespace std;

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
const int MX = 120;
int t, h, w;
string keystr;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> t;
    while(t--){
        cin >> h >> w;
        queue<pair<int, int>> Q;
        vector<pair<int, int>> door[26];
        char board[MX][MX] = {0};
        int vis[MX][MX] = {0};
        int key[26] = {};
        int cnt = 0;

        for(int i = 1; i <= h; i++)
            for(int j = 1; j <= w; j++) cin >> board[i][j];
        cin >> keystr;

        for(auto c : keystr) key[c - 'a'] = 1;
        Q.push({0, 0});
        vis[0][0] = 1;
        while(!Q.empty()){
            auto cur = Q.front(); Q.pop();
            for(int dir = 0; dir < 4; dir++){
                int nx = cur.X + dx[dir];
                int ny = cur.Y + dy[dir];
                if(nx < 0 || nx > h + 1 || ny < 0 || ny > w + 1) continue;
                if(vis[nx][ny] || board[nx][ny] == '*') continue;
                vis[nx][ny] = 1;
                if(board[nx][ny] >= 'a' && board[nx][ny] <= 'z'){
                    int k = board[nx][ny] - 'a';
                    key[k] = 1;
                    for(auto door_pair : door[k])  {
                        Q.push(door_pair);
                        vis[door_pair.first][door_pair.second] = 1;
                    }
                }
                else if(board[nx][ny] >= 'A' && board[nx][ny] <= 'Z'){
                    int k = board[nx][ny] + 32 - 'a';
                    if (!key[k]){
                        door[k].push_back({nx, ny});
                        continue;
                    }
                }
                else if(board[nx][ny] == '$') cnt++;
                Q.push({nx, ny});
            }
        }
        cout << cnt << "\n";
    }
}