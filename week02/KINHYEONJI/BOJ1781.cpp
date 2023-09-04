#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;
    priority_queue<int, vector<int>> pq;
    vector<vector<int>> v(200002);
    int max_deadline = 0;
    for (int i = 0; i < n; i++) {
        int deadline, cnt;
        cin >> deadline >> cnt;
        if (deadline > max_deadline) max_deadline = deadline;
        v[deadline].push_back(cnt);
    }
    int answer = 0;
    for (int i = max_deadline; i > 0; i--) {
        for (int noodle: v[i]) {
            pq.push(noodle);
        }
        if (pq.empty())continue;
        answer += pq.top();
        pq.pop();
    }
    cout << answer;
}