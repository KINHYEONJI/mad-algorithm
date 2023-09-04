#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(string a, string b) {
    if (a.length() == b.length())
        return a < b;
    return a.length() < b.length();
}

int main() {
    int n;
    cin >> n;
    vector<string> find_num;
    for (int i = 0; i < n; i++) {
        string str;
        cin >> str;
        string find_str = "";
        for (int j = 0; j < str.size(); j++) {
            if (str[j] >= '0' && str[j] <= '9') find_str += str[j];
            else {
                if(find_str == "") continue;
                int k;
                if (find_str != "") {
                    for (k = 0; k < find_str.size(); k++) {
                        if (find_str[k] != '0') break;
                    }
                }
                if (k == find_str.size()) find_str = "0";
                else find_str.erase(0, k);
                find_num.push_back(find_str);
                find_str = "";
            }
        }
        if (find_str != "") {
            int k;
            for (k = 0; k < find_str.size(); k++) {
                if (find_str[k] != '0') break;
            }
            if (k == find_str.size()) find_str = "0";
            else find_str.erase(0, k);
            find_num.push_back(find_str);
        }
    }
    if (!find_num.empty())
        sort(find_num.begin(), find_num.end(), cmp);

    for (string str: find_num) cout << str << '\n';
}

