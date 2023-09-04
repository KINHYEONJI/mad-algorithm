#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>

using namespace std;

int main() {
    int m, n;
    cin >> m >> n;
    int t;
    cin >> t;
    vector<int> dd;
    for (int i = 0; i < t + 1; i++) {
        int direction, distance;
        cin >> direction >> distance;
        if (direction == 1) dd.push_back(distance);
        else if (direction == 2)dd.push_back(2 * m + n - distance);
        else if (direction == 3) dd.push_back(2 * (m + n) - distance);
        else if (direction == 4) dd.push_back(m + distance);
    }
    int sum_ = 0;
    for (int i = 0; i < t; i++) {
        sum_ += min(abs(dd[t] - dd[i]), 2 * (m + n) - abs(dd[t] - dd[i]));
    }
    cout << sum_;
}