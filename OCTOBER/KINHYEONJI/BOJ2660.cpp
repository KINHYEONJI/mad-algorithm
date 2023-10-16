#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n;
int arr[51][51];

int main() {
    cin >> n;
    fill(&arr[1][1], &arr[n][n + 1], 0x3f3f3f);
    while (true) {
        int a, b;
        cin >> a >> b;
        if (a == -1 && b == -1) break;
        arr[a][b] = 1;
        arr[b][a] = 1;
    }
    for (int k = 1; k <= n; k++) {
        for (int i = 1; i <= n; i++) {
            if (k == i) continue;
            for (int j = 1; j <= n; j++) {
                if (i == j || k == j) continue;
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j]);
            }
        }
    }
    int min_score = 50;
    vector<int> v;
    for (int i = 1; i <= n; i++) {
        int score = 0;
        for (int j = 1; j <= n; j++) {
            if (i == j) continue;
            score = max(score, arr[i][j]);
        }
        if (score < min_score) {
            min_score = score;
            v.clear();
            v.push_back(i);
        } else if (score == min_score) {
            v.push_back(i);
        }
    }
    cout << min_score <<" "<<v.size()<<'\n';
    for(int vv : v) cout<<vv<<" ";
}