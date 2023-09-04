#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main(){
    int n, m;
    cin>>n>>m;
    vector<int> adj[32001];
    int deg[32001];
    while(m--){
        int a, b;
        cin>>a>>b;
        adj[a].push_back(b);
        deg[b]++;
    }
    queue<int> q;
    for(int i = 1; i<=n; i++){
        if(!deg[i]) q.push(i);
    }
    while(!q.empty()){
        int cur = q.front();
        q.pop();
        cout<<cur<<" ";
        for(int nxt : adj[cur]){
            deg[nxt]--;
            if(!deg[nxt]) q.push(nxt);
        }
    }
}