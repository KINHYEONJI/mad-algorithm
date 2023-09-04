#include <iostream>

using namespace std;

int main() {
    int N;
    cin >> N;
    int paper[100][100] = {};
    for (int i = 0; i < N; i++) {
        int x, y;
        cin >> x >> y;
        for (int i = x; i < x + 10; i++) {
            for (int j = y; j < y + 10; j++) {
                paper[i][j] = 1;
            }
        }
    }
    int count = 0;
    for (int i = 0; i < 100; i++) {
        for (int j = 0; j < 100; j++) {
            if (paper[i][j]) count++;
        }
    }
    cout << count;
}