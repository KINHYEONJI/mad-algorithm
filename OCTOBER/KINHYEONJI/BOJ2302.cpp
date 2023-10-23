#include <iostream>
#include <vector>

using namespace std;

vector<int> v = {0};
int d[45];

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, m, vv;
    cin >> n;
    cin >> m;
    while (m--) {
        cin >> vv;
        v.push_back(vv);
    }
    v.push_back(n + 1);

    d[0] = 1;
    d[1] = 1;
    d[2] = 2;
    for (int i = 3; i <= n; i++) d[i] = d[i - 1] + d[i - 2];

    int ans = 1;
    for (int i = 1; i < v.size(); i++) ans *= d[v[i] - v[i - 1] - 1];
    cout << ans;
}