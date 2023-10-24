#include <iostream>
#include <tuple>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

priority_queue<tuple<int, int, int>,
        vector<tuple<int, int, int>>,
        greater<>> pq;
vector<pair<int, int>> adj[100002];
bool visited[100002];
int n, m;
int a, b, c;

int main() {
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        cin >> a >> b >> c;
        adj[a].emplace_back(c, b);
        adj[b].emplace_back(c, a);
    }
    visited[1] = 1;
    for (auto nxt: adj[1]) {
        pq.emplace(nxt.first, 1, nxt.second);
    }

    int cnt = 0;
    int answer = 0;
    int mc = 0;
    while (cnt < n - 1) {
        tie(c, a, b) = pq.top();
        pq.pop();
        if (visited[b]) continue;

        visited[b] = 1;
        answer += c;
        mc = max(mc, c);
        cnt++;

        for (auto nxt: adj[b]) {
            if (!visited[nxt.second]) {
                pq.emplace(nxt.first, b, nxt.second);
            }
        }
    }
    cout << answer - mc;
}
