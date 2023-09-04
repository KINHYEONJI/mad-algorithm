#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    int x, y;
    vector<bool> visited(200001, false);
    queue<pair<int, int>> q;

    cin >> x >> y;
    q.push({x, 0});
    visited[x] = true;
    while (!q.empty()) {
        pair<int, int> cur = q.front();
        if (cur.first == y) {
            cout << cur.second;
            break;
        }
        q.pop();
        if (cur.first - 1 >= 0 && !visited[cur.first - 1]) {
            q.push({cur.first - 1, cur.second + 1});
            visited[cur.first - 1] = true;
        }
        if (cur.first + 1 <= y * 2 && !visited[cur.first + 1]) {
            q.push({cur.first + 1, cur.second + 1});
            visited[cur.first + 1] = true;
        }
        if (cur.first * 2 <= y * 2 &&  !visited[cur.first * 2]) {
            q.push({cur.first * 2, cur.second + 1});
            visited[cur.first * 2] = true;
        }
    }
    return 0;
}