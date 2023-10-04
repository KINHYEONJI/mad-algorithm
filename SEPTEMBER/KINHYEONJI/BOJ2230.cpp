#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> v(n, 0);
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }
    sort(v.begin(), v.end());
    int en = 0;
    int answer = 0x7fffffff;
    for (int st = 0; st < n; st++) {
        while (en < n && v[en] - v[st] < m) en++;
        if(en== n) break;
        answer = min(answer, v[en] - v[st]);
    }
    cout << answer;
}