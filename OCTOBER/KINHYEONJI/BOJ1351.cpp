#include <iostream>
#include <unordered_map>

using namespace std;

unordered_map<long long, long long> um;

long long dp(long long n, int p, int q) {
    if (n == 0) return 1;
    if (um.find(n) != um.end()) return um[n];
    um[n] = dp(n / p, p, q) + dp(n / q, p, q);
    return um[n];
}

int main() {
    long long n;
    int p, q;
    cin >> n >> p >> q;
    cout << dp(n, p, q) << endl;
    return 0;
}