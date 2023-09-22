#include <iostream>
#include <vector>
#include <algorithm>

#define INF 0x3f3f3f
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<vector<int>> v(n + 2, vector<int>(n + 2));
    vector<int> comb;
    for (int i = 0; i < n; i++) {
        if (i == k) continue;
        comb.push_back(i);
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> v[i][j];
        }
    }
    for (int l = 0; l < n; l++) {
        for (int i = 0; i < n; i++) {
            if (l == i) continue;
            for (int j = 0; j < n; j++) {
                if (l == j || i == j) continue;
                if (v[i][j] > v[i][l] + v[l][j]) {
                    v[i][j] = v[i][l] + v[l][j];
                }
            }
        }
    }
    int ans = 0x7f7f7f7f;
    do {
        int tmp = v[k][comb[0]];
        for (int i = 0; i < n - 2; i++) {
            tmp += v[comb[i]][comb[i + 1]];
        }
        ans = min(ans, tmp);
    } while (next_permutation(comb.begin(), comb.end()));

    cout << ans;
}