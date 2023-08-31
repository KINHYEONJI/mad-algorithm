#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
const int INF = 0x3f3f3f3f;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> v(n + 1, vector<int>(n + 1, INF));
    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        v[a][b] = min(v[a][b], c);
    }
    for(int i = 1; i<n+1; i++){
        v[i][i] = 0;
    }
    for (int i = 1; i < n + 1; i++) {
        for (int j = 1; j < n + 1; j++) {
            for (int k = 1; k < n + 1; k++) {
                v[j][k] = min(v[j][i] + v[i][k], v[j][k]);
            }
        }
    }
    for (int i = 1; i < n + 1; i++) {
        for (int j = 1; j < n + 1; j++) {
            if (v[i][j] == INF) cout << "0 ";
            else cout << v[i][j] << " ";
        }
        cout << '\n';
    }
}