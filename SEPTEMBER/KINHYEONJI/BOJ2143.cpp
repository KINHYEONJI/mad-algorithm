#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int t, n, m;
    cin >> t >> n;
    int v_n[1001];
    int v_m[1001];
    vector<int> prefix_n;
    for (int i = 1; i <= n; i++) {
        cin >> v_n[i];
    }
    cin >> m;
    vector<int> prefix_m;
    for (int i = 1; i <= m; i++) {
        cin >> v_m[i];
    }
    for (int i = 1; i <= n; i++) {
        int prefix_sum = v_n[i];
        prefix_n.push_back(prefix_sum);
        for (int j = i + 1; j <= n; j++) {
            prefix_sum += v_n[j];
            prefix_n.push_back(prefix_sum);
        }
    }
    for (int i = 1; i <= m; i++) {
        int prefix_sum = v_m[i];
        prefix_m.push_back(prefix_sum);
        for (int j = i + 1; j <= m; j++) {
            prefix_sum += v_m[j];
            prefix_m.push_back(prefix_sum);
        }
    }
    sort(prefix_m.begin(), prefix_m.end());
    long long ans = 0;
    for (auto item: prefix_n) {
        int diff = t - item;
        auto ub = upper_bound(prefix_m.begin(), prefix_m.end(), diff);
        auto lb = lower_bound(prefix_m.begin(), prefix_m.end(), diff);
        ans += (ub - lb);
    }
    cout << ans;
}