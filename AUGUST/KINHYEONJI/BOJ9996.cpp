#include <iostream>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    string checkStr;
    cin >> checkStr;
    int index = checkStr.find("*");
    for (int i = 0; i < n; i++) {
        string fileName;
        cin >> fileName;
        int flag = 1;
        int visited[100] = {0};
        for (int j = 0; j < index; j++) {
            visited[j] = 1;
            if (checkStr[j] != fileName[j]) {
                flag = 0;
                break;
            }
        }
        for (int j = 0; j < checkStr.size() - index - 1; j++) {
            if (checkStr[checkStr.size() - j - 1] != fileName[fileName.size() - j - 1] ||
                visited[fileName.size() - j - 1]) {
                flag = 0;
                break;
            }
        }
        if (flag) cout << "DA" << '\n';
        else cout << "NE" << "\n";
    }
    return 0;
}
