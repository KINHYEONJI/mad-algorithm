#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, l;
    cin >> n >> l;
    vector<vector<int>> signal;
    signal.push_back({0, 0, 0});
    for (int i = 0; i < n; i++) {
        int d, r, g;
        cin >> d >> r >> g;
        signal.push_back({d, r, g});
    }
    int time = 0;
    for (int i = 1; i < n + 1; i++) {
        time += (signal[i][0] - signal[i - 1][0]);
        if (time % (signal[i][1] + signal[i][2]) <= signal[i][1])
            time += (signal[i][1] - (time % (signal[i][1] + signal[i][2])));
    }
    time += l - signal[n][0];
    cout << time;
}
