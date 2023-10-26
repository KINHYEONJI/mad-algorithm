#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
tt
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    vector<pair<int, int>> v;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int s, e;
        cin >> s >> e;
        v.push_back({s, e});
    }
    sort(v.begin(), v.end());
    int s = v[0].first;
    int e = v[0].second;
    int answer = 0;
    int i = 0;
    while (i < n) {
        if (v[i].first > e) {
            answer += e - s;
            s = v[i].first;
            e = v[i].second;
        } else if (v[i].first <= e && v[i].second > e) {
            e = v[i].second;
        }
        i++;
    }
    answer += e - s;
    cout << answer;
}

