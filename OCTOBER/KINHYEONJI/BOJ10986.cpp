#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<long long> v(n + 1, 0);
    vector<long long> prefix_sum(n + 1, 0);
    map<long long, long long> mm;
    long long cnt = 0;
    for (long long i = 1; i <= n; i++) {
        cin >> v[i];
        prefix_sum[i] = prefix_sum[i - 1] + v[i];
        if(prefix_sum[i] % m == 0) cnt++;
    }
    for (long long i = 1; i <= n; i++) {
        cnt += mm[prefix_sum[i] % m];
        mm[prefix_sum[i] % m]++;
    }
    cout << cnt;
}