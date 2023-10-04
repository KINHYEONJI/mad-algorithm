#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
    long long n, k;
    cin >> n >> k;
    vector<long long> v(n, 0);
    map<long long, long long> m;
    for (long long i = 0; i < n; i++) {
        cin >> v[i];
    }
    vector<long long> prefix_sum(n + 1, 0);
    long long cnt = 0;
    for (long long i = 1; i <= n; i++) {
        prefix_sum[i] += prefix_sum[i - 1] + v[i-1];
        if (prefix_sum[i] == k) cnt++;
    }
    for(int i = 1; i<=n; i++){
        cnt += m[prefix_sum[i] - k];
        m[prefix_sum[i]]++;
    }
    cout << cnt;
}
