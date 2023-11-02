#include <iostream>
#include <algorithm>

using namespace std;

int increase_dp[1002];
int decrease_dp[1002];
int n;
int arr[1002];

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        increase_dp[i] = 1;
        decrease_dp[i] = 1;
    }

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] < arr[j]) {
                increase_dp[j] = max(increase_dp[i] + 1, increase_dp[j]);
            }
        }
    }

    for (int i = n - 1; i >= 0; i--) {
        for (int j = i - 1; j >= 0; j--) {
            if (arr[i] < arr[j]) {
                decrease_dp[j] = max(decrease_dp[i] + 1, decrease_dp[j]);
            }
        }
    }

    int max_len = 0;
    for (int i = 0; i < n; i++) {
        max_len = max(max_len, increase_dp[i] + decrease_dp[i] - 1);
    }

    cout<<max_len;

}