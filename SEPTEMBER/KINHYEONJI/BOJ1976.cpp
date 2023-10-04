#include <iostream>

using namespace std;
int n, m;
int parent[201];

int find_(int a) {
    if (a == parent[a]) return a;
    return parent[a] = find_(parent[a]);
}

void union_(int a, int b) {
    a = find_(a);
    b = find_(b);
    parent[a] = b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> n >> m;
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            int num;
            cin >> num;
            if (j <= i) continue;
            if (!num) continue;
            union_(i, j);
        }
    }

    int past, here;
    cin >> past;
    for (int i = 0; i < m - 1; i++) {
        cin >> here;
        if (find_(past) != find_(here)) {
            cout << "NO";
            return 0;
        }
        past = here;
    }
    cout << "YES";
}