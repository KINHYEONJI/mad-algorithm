#include <iostream>
#include <algorithm>

using namespace std;
int arr[1002];
int n;

void dfs(int cnt) {
    if (cnt > n) return;
    if (arr[cnt + 1] > arr[cnt] + 1) {
        arr[cnt + 1] = arr[cnt] + 1;
        dfs(cnt + 1);
    }
    if (arr[cnt + 3] > arr[cnt] + 1) {
        arr[cnt + 3] = arr[cnt] + 1;
        dfs(cnt + 3);
    }
}

int main() {
    cin >> n;
    fill(arr, arr + n + 1, 0x3f3f3f);
    arr[0] = 0;
    dfs(0);

    if (arr[n] % 2 == 0) cout << "CY";
    else cout << "SK";
}