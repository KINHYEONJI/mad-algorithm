#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int parent[200002];
int node_count[200002];
unordered_map<string, int> um;

int Find(int a) {
    if (a == parent[a]) return a;
    return parent[a] = Find(parent[a]);
}

void Union(int a, int b) {
    a = Find(a);
    b = Find(b);
    if (a != b) {
        node_count[parent[a]] += node_count[parent[b]];
        parent[b] = a;
    }
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        int F;
        scanf("%d", &F);
        um.clear();
        for (int i = 0; i < 200002; i++) { //초기화
            parent[i] = i;
            node_count[i] = 1;
        }
        int index = 0;
        for (int f = 0; f < F; f++) {
            char str1[21], str2[21];
            scanf("%s %s", &str1, &str2);
            if (um.find(str1) == um.end()) {
                um[str1] = index;
                index++;
            }
            if (um.find(str2) == um.end()) {
                um[str2] = index;
                index++;
            }
            Union(um[str1], um[str2]);
            cout << node_count[parent[um[str1]]] << '\n';
        }
    }
}