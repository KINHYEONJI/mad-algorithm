#include <iostream>
#include <queue>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int n;
        cin >> n;
        priority_queue<long long, vector<long long>, greater<long long>> q;
        for (int i = 0; i < n; i++) {
            long long num;
            cin >> num;
            q.push(num);
        }
        long long answer = 0;
        for (int i = 0; i < n - 1; i++) {
            long long num1 = q.top();
            q.pop();
            long long num2 = q.top();
            q.pop();
            answer += num1 + num2;
            q.push(num1 + num2);
        }
        cout<<answer<<'\n';
    }
}