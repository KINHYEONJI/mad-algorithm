#include <iostream>

using namespace std;

int main() {
    int num;
    cin >> num;
    int count = 0;
    int firstNum = num;
    while (true) {
        int newNum = num % 10 * 10 + (num / 10 + num % 10) % 10;
        count++;
        if (newNum == firstNum) {
            cout << count;
            return 0;
        }
        num = newNum;
    }
    return 0;
}