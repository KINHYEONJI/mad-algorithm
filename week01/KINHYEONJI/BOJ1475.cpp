
#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string str;
    cin >> str;
    vector<int> numlist;
    for (char ch: str) {
        numlist.push_back(ch - '0');
    }
    int countArr[10] = {};
    for (int i = 0; i < numlist.size(); i++) {
        countArr[numlist[i]]++;
    }
    int maxCount = round(double((countArr[6] + countArr[9])) / 2);

    for (int i = 0; i < 10; i++) {
        if (i == 6 || i == 9) continue;
        maxCount = max(maxCount, countArr[i]);
    }
    cout << maxCount;
    return 0;
}