#include <iostream>
#include <deque>
#include <array>

using namespace std;

void rotate1(deque<int> &dq) {
    int back = dq.back();
    dq.pop_back();
    dq.push_front(back);
}

void rotate_1(deque<int> &dq) {
    int front = dq.front();
    dq.pop_front();
    dq.push_back(front);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    array<deque<int>, 4> arr;
    for (int i = 0; i < 4; i++) {
        string str;
        cin >> str;
        for (int j = 0; j < 8; j++) {
            arr[i].push_back(str[j] - '0');
        }
    }
    int k;
    cin >> k;
    for (int i = 0; i < k; i++) {
        int n, dir;
        cin >> n >> dir;
        array<int, 4> rotate_index = {0, 0, 0, 0};

        rotate_index[n - 1] = dir;

        //자신 기준 왼쪽 톱니바퀴 회전
        for (int j = 1; j < n; j++) {
            if (arr[n - j][6] != arr[n - j - 1][2]) {
                if (rotate_index[n - j] == -1) rotate_index[n - j - 1] = 1;
                else rotate_index[n - j - 1] = -1;
            } else break;
        }

        //자신 기준 오른쪽 톱니바퀴 회전
        for (int j = 1; j < 4 - n + 1; j++) {
            if (arr[n - 2 + j][2] != arr[n - 1 + j][6]) {
                if (rotate_index[n - 2 + j] == -1) rotate_index[n - 1 + j] = 1;
                else rotate_index[n - 1 + j] = -1;
            } else break;
        }

        for (int j = 0; j < 4; j++) {
            if (rotate_index[j] == -1) {
                rotate_1(arr[j]);
            } else if (rotate_index[j] == 1) {
                rotate1(arr[j]);
            }
        }
    }
    cout << arr[0][0] * 1 + arr[1][0] * 2 + arr[2][0] * 4 + arr[3][0] * 8;

}