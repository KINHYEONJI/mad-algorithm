#include <iostream>
#include <vector>
#include <algorithm>

#define X first
#define Y second

using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    vector<pair<int, int>> flower;
    for (int i = 0; i < n; i++) {
        int sm, sd, em, ed;
        cin >> sm >> sd >> em >> ed;
        flower.push_back({sm * 100 + sd, em * 100 + ed});
    }

    sort(flower.begin(), flower.end());

    int t = 301;
    int ans = 0;
    int idx = 0;

    while (t < 1201) {
        int max_end = t;
        while (idx < n && flower[idx].X <= t) {
            max_end = max(max_end, flower[idx].Y);
            idx++;
        }

        if (max_end == t) {
            cout << 0;
            return 0;
        }

        ans++;
        t = max_end;
    }

    cout << ans;
}
