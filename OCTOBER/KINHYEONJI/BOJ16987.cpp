#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int n;
pair<int, int> p[8];
vector<int> broken(8, 0);
int max_cnt = 0;

void dfs(int index, int cnt) {
    if (index == n) {
        max_cnt = max(cnt, max_cnt);
        return;
    }
    if (p[index].first <= 0 or cnt == n - 1) {
        dfs(index + 1, cnt);
        return;
    }
    for (int i = 0; i < n; i++) {
        if (i== index || broken[i]) continue;
        int after_cnt = cnt;
        p[index].first -= p[i].second;
        p[i].first -= p[index].second;
        if (p[index].first <= 0) {
            broken[index] = 1;
            after_cnt++;
        }
        if (p[i].first <= 0) {
            broken[i] = 1;
            after_cnt++;
        }
        dfs(index + 1, after_cnt);
        p[index].first += p[i].second;
        p[i].first += p[index].second;
        if (p[index].first > 0)
            broken[index] = 0;
        if (p[i].first > 0)
            broken[i] = 0;
    }
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        int s, w;
        cin >> s >> w;
        p[i] = {s, w};
    }
    dfs(0, 0);
    cout << max_cnt;
}