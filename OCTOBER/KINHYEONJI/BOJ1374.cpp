#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int n, room, from, to, answer = 0;

vector<pair<int, int>> v;
priority_queue<int, vector<int>, greater<int>> lastTime;

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> room >> from >> to;
        v.push_back({from, to});
    }
    sort(v.begin(), v.end());

    for (int i = 0; i < n; i++) {
        int startTime = v[i].first;
        int endTime = v[i].second;

        if (lastTime.empty()) {
            lastTime.push(endTime);
            answer++;
        } else {
            if (lastTime.top() > startTime) {
                answer++;
            } else {
                lastTime.pop();
            }
            lastTime.push(endTime);
        }
    }
    cout << answer;
}