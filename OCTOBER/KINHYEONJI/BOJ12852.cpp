#include <iostream>
#include <algorithm>
#include <stack>

using namespace std;

int n;
int dp[1000002];
int mem[1000002];

void dfs(int num) {
    if (num <= 1) return;
    if (num % 3 == 0 && dp[num / 3] > dp[num] + 1) {
        dp[num / 3] = dp[num] + 1;
        mem[num / 3] = num;
        dfs(num / 3);
    }
    if (num % 2 == 0 && dp[num / 2] > dp[num] + 1) {
        dp[num / 2] = dp[num] + 1;
        mem[num / 2] = num;
        dfs(num / 2);
    }
    if (dp[num - 1] > dp[num] + 1) {
        dp[num - 1] = dp[num] + 1;
        mem[num - 1] = num;
        dfs(num - 1);
    }
}

int main() {
    cin >> n;
    fill(dp, dp + 1000002, 0x3f3f3f3f);
    dp[n] = 0;
    dfs(n);
    cout << dp[1] << '\n';
    stack<int> st;
    int before_num = 1;
    st.push(before_num);
    while (before_num != n) {
        st.push(mem[before_num]);
        before_num = mem[before_num];
    }
    while (!st.empty()) {
        cout << st.top() << " ";
        st.pop();
    }
}