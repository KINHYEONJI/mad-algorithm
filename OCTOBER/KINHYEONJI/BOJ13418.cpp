#include <iostream>
#include <queue>
#include <vector>
#include <tuple>

using namespace std;

priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<>> g_pq;
priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, less<>> l_pq;
bool visited[1002];
vector<pair<int, int>> adj[1002];
int n, m, a, b, c;

int main() {
    cin >> n >> m;
    for (int i = 0; i < m + 1; i++) {
        cin >> a >> b >> c;
        adj[a].push_back({c, b});
        adj[b].push_back({c, a});
    }

    for (auto nxt: adj[0]) {
        g_pq.push({nxt.first, 0, nxt.second});
        l_pq.push({nxt.first, 0, nxt.second});
    }

    fill(visited, visited + n + 1, false);
    visited[0] = true;
    int max_answer = 0;
    int max_cnt = 0;

    while (max_cnt < n) {
        tie(c, a, b) = g_pq.top();
        g_pq.pop();
        if (visited[b]) continue;

        visited[b] = true;
        max_answer += !c;
        max_cnt++;

        for (auto nxt: adj[b]) {
            if (visited[nxt.second]) continue;
            g_pq.push({nxt.first, b, nxt.second});
        }
    }

    fill(visited, visited + n + 1, false);
    visited[0] = true;
    int min_answer = 0;
    int min_cnt = 0;

    while (min_cnt < n) {
        tie(c, a, b) = l_pq.top();
        l_pq.pop();
        if (visited[b]) continue;

        visited[b] = true;
        min_answer += !c;
        min_cnt++;

        for (auto nxt: adj[b]) {
            if (visited[nxt.second]) continue;
            l_pq.push({nxt.first, b, nxt.second});
        }
    }
    cout << max_answer * max_answer - min_answer * min_answer;
}
