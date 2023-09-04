#include <iostream>
#include <vector>

using namespace std;

bool check_bingo(int arr[5][5]) {
    int count = 0;
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            if (arr[i][j] != 0) break;
            if (j == 4) count++;
        }
    }

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            if (arr[j][i] != 0) break;
            if (j == 4) count++;
        }
    }

    for (int i = 0; i < 5; i++) {
        if (arr[i][4 - i] != 0) break;
        if (i == 4) count++;
    }

    for (int i = 0; i < 5; i++) {
        if (arr[i][i] != 0) break;
        if (i == 4) count++;
    }

    if (count >= 3) return true;
    else return false;
}

int main() {
    int arr[5][5];
    int num[26][2] = {};
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            cin >> arr[i][j];
            num[arr[i][j]][0] = i;
            num[arr[i][j]][1] = j;
        }
    }


    for (int i = 0; i < 25; i++) {
        int call_num;
        cin >> call_num;
        int x = num[call_num][0];
        int y = num[call_num][1];
        arr[x][y] = 0;
        if (check_bingo(arr)) {
            cout << i + 1;
            return 0;
        }
    }
}