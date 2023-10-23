#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    long long arr[1000002];
    arr[1] = 1;
    arr[2] = 2;
    arr[3] = 4;
    for (int i = 4; i < 1000001; i++) {
        arr[i] = (arr[i - 1] + arr[i - 2] + arr[i - 3]) % 1000000009;
    }
    int cnt;
    cin >> cnt;
    while (cnt--) {
        int num;
        cin >> num;
        cout << arr[num] << '\n';
    }
}