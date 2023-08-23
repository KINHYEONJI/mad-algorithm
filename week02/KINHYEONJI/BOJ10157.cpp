#include <iostream>
#include <vector>

using namespace std;

int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};

int main() {
    int r, c, target;
    cin >> c >> r >> target;
    vector<vector<int>> room(r + 2, vector<int>(c + 2, 0));
    if (target > c * r) {
        cout << 0;
        return 0;
    }

    for (int i = 0; i < c + 2; i++) {
        room[0][i] = 1;
        room[r + 1][i] = 1;
    }
    for (int i = 0; i < r + 2; i++) {
        room[i][0] = 1;
        room[i][c + 1] = 1;
    }

    int cnt = 1;
    int s_x = 0;
    int s_y = 1;
    int dir = 0;

    while (true) {
        while (true) {
            s_x += dx[dir];
            s_y += dy[dir];
            if (!room[s_x][s_y]) {
                room[s_x][s_y] = cnt++;
            } else {
                s_x -= dx[dir];
                s_y -= dy[dir];
                break;
            }
            if (cnt == target + 1) {
                cout << s_y << " " << s_x;
                return 0;
            }
        };
        dir = (dir + 1) % 4;
    }
}