#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> v_h(n + 1);
    vector<int> memory(n + 1, 0);
    for (int i = 0; i < n; i++) {
        cin >> v_h[i + 1];
    }
    for (int i = 0; i < m; i++) {
        int s, e, h;
        cin >> s >> e >> h;
        memory[s] += h;
        if (e < n) memory[e + 1] -= h;
    }
    for (int i = 1; i < n; i++) {
        memory[i + 1] += memory[i];
    }
    for (int i = 1; i <= n; i++) {
        cout << v_h[i] + memory[i] << " ";
    }
}