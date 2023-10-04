#include <iostream>
#include <vector>

#define INF 0x3f3f3f
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin >> N;
    vector<vector<int>> v(N + 1, vector<int>(N + 1, INF));
    vector<vector<int>> nxt(N + 1, vector<int>(N + 1));
    int m;
    cin >> m;
    while (m--) {
        int a, b, c;
        cin >> a >> b >> c;
        if (v[a][b] > c) {
            v[a][b] = c;
            nxt[a][b] = b;
        }
    }
    for (int k = 1; k < N + 1; k++) {
        for (int i = 1; i < N + 1; i++) {
            if (k == i) continue;
            for (int j = 1; j < N + 1; j++) {
                if (i == j || k == j) continue;
                if (v[i][j] > v[i][k] + v[k][j]) {
                    v[i][j] = v[i][k] + v[k][j];
                    nxt[i][j] = nxt[i][k];
                }
            }
        }
    }

    for (int i = 1; i < N + 1; i++) {
        for (int j = 1; j < N + 1; j++) {
            if (v[i][j] == INF) cout << "0 ";
            else cout << v[i][j] << " ";
        }
        cout << '\n';
    }

    for (int i = 1; i < N + 1; i++) {
        for (int j = 1; j < N + 1; j++) {
            int cnt = 0;
            int s = i;
            int e = j;
            vector<int> memory_;
            while (nxt[s][e] != 0 && nxt[s][e] != j) {
                s = nxt[s][e];
                cnt++;
                memory_.push_back(s);
            }
            if (v[i][j] == INF) cout << "0" << '\n';
            else {
                cout << cnt + 2 << " " << i << " ";
                for (auto node: memory_) cout << node << " ";
                cout << j << '\n';
            }
        }

    }
    return 0;
}