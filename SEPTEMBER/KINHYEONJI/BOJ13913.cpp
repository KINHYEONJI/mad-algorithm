#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> v(200002, -1);
    vector<int> memory(200002, -1);
    queue<int> q;
    stack<int> st;
    q.push(n);
    st.push(n);
    v[n] = 0;
    memory[n] = n;

    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        if (cur == k) break;
        int next[3] = {cur + 1, cur - 1, cur * 2};
        for (int i = 0; i < 3; i++) {
            if (next[i] >= 0 && next[i] <= 200000 && v[next[i]] == -1) {
                v[next[i]] = v[cur] + 1;
                memory[next[i]] = cur;
                q.push(next[i]);
            }
        }
    }

    cout << v[k] << '\n';

    stack<int> path;
    int cur = k;
    while (cur != n) {
        path.push(cur);
        cur = memory[cur];
    }
    path.push(n);

    while (!path.empty()) {
        cout << path.top() << ' ';
        path.pop();
    }

    return 0;
}
