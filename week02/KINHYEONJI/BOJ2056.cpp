#include <bits/stdc++.h>
using namespace std;

int n, ans;
int dur[10002];
int ind[10002];
vector<int> rel[100002];
vector<int> tt[1000002];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for(int i = 1; i <= n; i++) {
        cin >> dur[i];
        int m; cin >> m;
        if(!m) tt[dur[i]].push_back(i);
        while(m--) {
            int x; cin >> x;
            rel[x].push_back(i);
            ind[i]++;
        }
    }

    for(int t = 0; t <= 1000000; t++) {
        for(int finished : tt[t]) {
            ans = t;
            for(int r : rel[finished]) {
                ind[r]--;
                if(ind[r] != 0) continue;
                tt[t + dur[r]].push_back(r);
            }
        }
    }
    cout << ans;
}