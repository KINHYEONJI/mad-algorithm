#include <iostream>
#include <vector>

using namespace std;

void multipleChange(vector<bool> &arr, int n, int switchNum) {
    for (int i = switchNum - 1; i < n; i += switchNum) {
        arr[i] = !arr[i];
    }
}

void symmetryChange(vector<bool> &arr, int n, int switchNum) {
    arr[switchNum - 1] = !arr[switchNum - 1];
    int left = switchNum - 2;
    int right = switchNum;
    while (left >= 0 && right < n && arr[left] == arr[right]) {
        arr[left] = !arr[left];
        arr[right] = !arr[right];
        left--;
        right++;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    vector<bool> switchArr;
    for (int i = 0; i < n; i++) {
        bool b;
        cin >> b;
        switchArr.push_back(b);
    }

    int studentNum;
    cin >> studentNum;
    for (int i = 0; i < studentNum; i++) {
        int gender, switchNum;
        cin >> gender >> switchNum;

        if (gender == 1)
            multipleChange(switchArr, n, switchNum);
        else
            symmetryChange(switchArr, n, switchNum);
    }

    for (int i = 0; i < n; i++) {
        cout << switchArr[i] << " ";
        if ((i + 1) % 20 == 0 || i == n - 1)  // Print a newline after every 20 switches or at the end.
            cout << "\n";
    }

    return 0;
}