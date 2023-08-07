#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    string str;
    string findStr;
    getline(cin, str);
    getline(cin, findStr);

    int count = 0;
    int index = str.find(findStr);

    while (index != -1) {
        str.erase(0, index + findStr.length());
        count++;
        index = str.find(findStr);
    }

    cout << count;

    return 0;
}