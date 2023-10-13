#include <iostream>
#include <algorithm>

using namespace std;

int dp[1500002] = {0};
int n;
int max_cnt;
int main() {
    cin >> n;
    for (int i = 1; i <= n; i++) {
        int t, p;
        cin >> t >> p;
        if (i + t - 1 <= n) {
            dp[i + t - 1] = max(dp[i-1] + p, dp[i + t - 1]);
        }
        dp[i] = max(dp[i-1], dp[i]);
    }
    cout << dp[n];
}