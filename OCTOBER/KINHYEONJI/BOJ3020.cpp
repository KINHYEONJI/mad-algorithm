#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, h;
    cin >> n >> h;
    vector<int> top(h + 1, 0);
    vector<int> bottom(h + 1, 0);
    for (int i = 0; i < n; i += 2) {
        int bottom_num, top_num;
        cin >> bottom_num >> top_num;
        bottom[bottom_num]++;
        top[h - top_num + 1]++;
    }

    for (int i = h - 1; i > 0; i--) {
        bottom[i] += bottom[i + 1];
    }

    for (int i = 1; i <= h; i++) {
        top[i] += top[i - 1];
    }
    int min_break = 21e8;
    int cnt = 0;
    for (int i = 1; i <= h; i++) {
        if (min_break == bottom[i] + top[i]) {
            cnt++;
        } else {
            if (min_break > bottom[i] + top[i]) {
                cnt = 1;
                min_break = bottom[i] + top[i];
            }
        }
    }
    cout << min_break << " " << cnt;
}