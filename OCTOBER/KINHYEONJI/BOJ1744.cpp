#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
vector<int> v_plus;
vector<int> v_minus;
long long answer = 0;

void solve(vector<int> &v) {
    if(v.size()>1){
        for (int i = 0; i < v.size() - 1; i += 2) {
            answer += v[i] * v[i + 1];
        }
    }
    if (v.size() % 2 == 1) answer += v[v.size() - 1];
}

int main() {
    int n;
    cin >> n;
    while (n--) {
        int num;
        cin >> num;
        if (num == 1) answer += 1;
        else if (num > 0) v_plus.push_back(num);
        else v_minus.push_back(num);
    }
    sort(v_plus.begin(), v_plus.end(), greater<>());
    sort(v_minus.begin(), v_minus.end());
    solve(v_plus);
    solve(v_minus);
    cout << answer;
}