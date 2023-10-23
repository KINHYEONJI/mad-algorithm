#include <iostream>
#include <algorithm>

using namespace std;

int d[1005];
string ans[] = {"SK", "CY"};
int cand[] = {1, 3, 4};

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    fill(d, d + 1005, -1);
    d[1] = 0;
    d[2] = 1;
    d[3] = 0;
    d[4] = 0;

    for (int i = 5; i <= n; i++) {
        for (int j : cand) {
            if (d[i - j] == 1) {
                d[i] = 0; break;
            }
            else d[i] = 1;
        }
    }

    cout << ans[d[n]];
}