#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<bool>> adj(n + 1, vector<bool>(n + 1, false));
    int deg[32002] = {0};
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        adj[a][b] = true;
        deg[b]++;
    }
    vector<int> v(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        if (!deg[i]) {
            v[i] = 1;
        }
    }
    vector<int> answer;
    while (answer.size() < n) {
        int cur;
        for (int i = 1; i <= n; i++) {
            if (v[i]) {
                cur = i;
                v[i] = 0;
                answer.push_back(i);
                break;
            }
        }
        for (int j = 1; j <= n; j++) {
            if (adj[cur][j]) {
                adj[cur][j] = false;
                deg[j]--;
                if (!deg[j]) v[j] = 1;
            }
        }
    }
    for (int i = 0; i < n; i++) {
        cout << answer[i] << " ";
    }
}