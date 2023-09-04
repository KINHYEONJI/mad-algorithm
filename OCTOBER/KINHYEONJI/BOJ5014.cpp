#include <iostream>
#include <queue>

using namespace std;



int main() {
    int s, g, f, u, d;
    int visited[1000001] = {0};
    cin >> f >> s >> g >> u >> d;
    queue<int> q;
    q.push(s);
    visited[s] = 1;
    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        if (cur == g) break;
        if (cur + u <= f && !visited[cur + u]) {
            q.push(cur + u);
            visited[cur + u] = visited[cur] + 1;
        }
        if (cur - d >= 1 && !visited[cur - d]) {
            q.push(cur - d);
            visited[cur - d] = visited[cur] + 1;
        }
    }
    if (visited[g]) cout << visited[g] - 1;
    else cout << "use the stairs";
}