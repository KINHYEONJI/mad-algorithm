#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int n;
int arr[500'002];
int record[500'002];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> n;
    int total_cnt = 0;
    for (int i = 0; i < n; i++) {
        int index, value;
        cin >> index >> value;
        arr[index] = value;
        total_cnt = max(total_cnt, max(index, value));
    }
    vector<int> increase_v;
    increase_v.push_back(0);
    for (int i = 1; i <= total_cnt; i++) {
        if (arr[i] != 0) {
            increase_v.push_back(arr[i]);
            record[i] = 1;
            break;
        }
    }
    for (int i = 2; i <= total_cnt; i++) {
        if (arr[i] == 0) continue;
        if (*(increase_v.end() - 1) < arr[i]) {
            increase_v.push_back(arr[i]);
            record[i] = increase_v.size() - 1;
        } else {
            int index = lower_bound(increase_v.begin(), increase_v.end(), arr[i]) - increase_v.begin();
            increase_v[index] = arr[i];
            record[i] = index;
        }
    }
    cout << n - increase_v.size() + 1 << '\n';
    int check_index = increase_v.size() - 1;
    vector<int> increase_index(check_index);
    for (int i = total_cnt; i >= 1; i--) {
        if(check_index <= 0) break;
        if (record[i] == check_index) {
            increase_index[check_index - 1] = i;
            check_index--;
        }
    }
    int s = 0;
    for (int i = 1; i <= total_cnt; i++) {
        if (i == increase_index[s]) {
            s++;
        } else if (arr[i] == 0)continue;
        else {
            cout << i << '\n';
        }
    }
}