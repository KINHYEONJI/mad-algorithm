#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, k;
    vector<int> v;
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        v.push_back(num);
    }

    int window_sum = 0;
    for (int i = 0; i < k; i++) {
        window_sum += v[i];
    }
    int max_sum = window_sum;

    for (int i = k; i < n; i++) {
        window_sum += v[i] - v[i - k];
        max_sum = max(max_sum, window_sum);
    }

    cout << max_sum;
}
