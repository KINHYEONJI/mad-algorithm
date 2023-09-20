#include <iostream>
#include <vector>
#include <algorithm>

#define INF 0x3f3f3f
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> v(n + 1, vector<int>(n + 1, INF));
    for (int i = 0; i < m; i++) {
        int s, e, w;
        cin >> s >> e >> w;
        v[s][e] = w;
    }
    for (int l = 1; l < n + 1; l++) {
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                v[i][j] = min(v[i][j], v[i][l] + v[l][j]);
            }
        }
    }
    for (int i = 1; i < n + 1; i++) {
        v[i][i] = 0;
    }

    int k;
    cin >> k;
    vector<int> friends(k);
    for (int i = 0; i < k; i++) {
        cin >> friends[i];
    }
    int min_move = 0x7f7f7f;
    vector<int> ans;
    for (int i = 1; i < n + 1; i++) {
        int max_move_sum = 0;
        for (int j = 0; j < k; j++) {
            if (v[friends[j]][i] == INF || v[i][friends[j]] == INF) continue;
            max_move_sum = max(max_move_sum, v[friends[j]][i] + v[i][friends[j]]);
        }
        if (min_move > max_move_sum) {
            min_move = max_move_sum;
            ans.clear();
            ans.push_back(i);
        } else if (min_move == max_move_sum) {
            ans.push_back(i);
        }
    }
    sort(ans.begin(), ans.end());
    for (int a: ans) cout << a << " ";
}