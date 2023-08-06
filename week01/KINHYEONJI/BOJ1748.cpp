#include <iostream>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, count = 0;
    cin >> n;
    for (int i = 1; i <= n; i *= 10) {
        count += n - i +1;
    }
    cout<<count;
}