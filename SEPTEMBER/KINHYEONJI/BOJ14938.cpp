#include <iostream>
#include <vector>
#include <algorithm>

#define INF 0x3f3f3f
using namespace std;

int main() {
    int n, m, r;
    cin >> n >> m >> r;
    vector<int> t(102);
    for (int i = 1; i < n + 1; i++) {
        cin >> t[i];
    }
    vector<vector<int>> weight_table(n + 1, vector<int>(n + 1, INF));
    for (int i = 0; i < r; i++) {
        int s, e, w;
        cin >> s >> e >> w;
        weight_table[s][e] = w;
        weight_table[e][s] = w;
    }
    for (int k = 1; k < n + 1; k++) {
        for (int i = 1; i < n + 1; i++) {
            if (k == i) continue;
            for (int j = 1; j < n + 1; j++) {
                if (i == j || k == j) continue;
                if (weight_table[i][j] > weight_table[i][k] + weight_table[k][j]) {
                    weight_table[i][j] = weight_table[i][k] + weight_table[k][j];
                }
            }
        }
    }

    int max_item = 0;
    for (int i = 1; i < n + 1; i++) {
        int item_sum = t[i];
        for (int j = 1; j < n + 1; j++) {
            if (weight_table[i][j] <= m) item_sum += t[j];
        }
        max_item = max(max_item, item_sum);
    }
    cout << max_item;
}