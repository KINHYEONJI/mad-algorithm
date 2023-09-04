#include <iostream>
#include <vector>
#include <string>

using namespace std;

int n;
vector<vector<char>> v(50, vector<char>(50));

int cnt_long_candy() {
    int max_cnt = 0;
    for (int i = 0; i < n; i++) {
        int cnt = 0;
        char ch = 'A';
        for (int j = 0; j < n; j++) {
            if (v[i][j] == ch) cnt++;
            else {
                max_cnt = max(max_cnt, cnt);
                ch = v[i][j];
                cnt = 1;
            }
        }
        max_cnt = max(max_cnt, cnt);
    }


    for (int j = 0; j < n; j++) {
        int cnt = 0;
        char ch = 'A';
        for (int i = 0; i < n; i++) {
            if (v[i][j] == ch) cnt++;
            else {
                max_cnt = max(max_cnt, cnt);
                ch = v[i][j];
                cnt = 1;
            }
        }
        max_cnt = max(max_cnt, cnt);
    }
    return max_cnt;
}

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        string str;
        cin >> str;
        for (int j = 0; j < n; j++) {
            v[i][j] = str[j];
        }
    }
    int max_cnt = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (int dir = 0; dir < 4; dir++) {
                int nx = i + dx[dir];
                int ny = j + dy[dir];
                if (nx < 0 || ny < 0 || nx >= n || ny >= n)continue;
                if (v[i][j] != v[nx][ny]) {
                    char tmp = v[i][j];
                    v[i][j] = v[nx][ny];
                    v[nx][ny] = tmp;
                }
                int cnt = cnt_long_candy();
                max_cnt = max(max_cnt, cnt);
                char tmp = v[i][j];
                v[i][j] = v[nx][ny];
                v[nx][ny] = tmp;
            }
        }
    }
    cout<<max_cnt;
}