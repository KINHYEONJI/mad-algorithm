#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int l, c;
vector<char> arr;
vector<char> v;
int child_cnt = 0; //자음 개수는 c-2개 보다 많으면 안됨
int parent_cnt = 0; //모음 개수는 c-1개 보다 많으면 안됨

void dfs(int level, int last_index) {
    if (child_cnt > l - 2 || parent_cnt > l - 1) return;
    if (level == l) {
        for (auto ch: v) cout << ch;
        cout << '\n';
        return;
    }
    if (level > l) return;
    for (int i = last_index + 1; i < c; i++) {
        if (arr[i] == 'a' || arr[i] == 'e' || arr[i] == 'i' || arr[i] == 'o' || arr[i] == 'u') child_cnt++;
        else parent_cnt++;
        v.push_back(arr[i]);
        dfs(level + 1, i);
        if (arr[i] == 'a' || arr[i] == 'e' || arr[i] == 'i' || arr[i] == 'o' || arr[i] == 'u') child_cnt--;
        else parent_cnt--;
        v.pop_back();
    }
}

int main() {
    cin >> l >> c;
    for (int i = 0; i < c; i++) {
        char a;
        cin >> a;
        arr.push_back(a);
    }
    sort(arr.begin(), arr.end());
    dfs(0, -1);
}