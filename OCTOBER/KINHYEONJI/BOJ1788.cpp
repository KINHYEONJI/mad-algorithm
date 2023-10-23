#include <iostream>

using namespace std;

long long arr[1'000'002];

int main() {
    arr[0] = 0;
    arr[1] = 1;
    for (int i = 2; i < 1000001; i++) {
        arr[i] = (arr[i - 1] + arr[i - 2]) % 1'000'000'000;
    }
    int num;
    cin >> num;
    if (num > 0) {
        cout << 1 << '\n' << arr[num];

    } else if (num < 0) {
        if (abs(num) % 2 == 0) {
            cout << -1 << '\n' << arr[abs(num)];
        } else {
            cout << 1 << '\n' << arr[abs(num)];
        }
    } else {
        cout << 0 << '\n' << 0;
    }
}