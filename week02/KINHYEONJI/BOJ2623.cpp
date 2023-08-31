#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main(){
    int n, m;
    cin>>n>>m;
    vector<int> adj[1002];
    int deg[1002] = {0};
    while(m--){
        int cnt;
        cin>>cnt;
        vector<int> v;
        for(int i = 0; i<cnt; i++){
            int num;
            cin>>num;
            v.push_back(num);
        }
        for(int i = 1; i<v.size(); i++){
            adj[v[i-1]].push_back(v[i]);
            deg[v[i]]++;
        }
    }
    queue<int> q;
    vector<int> v;
    for(int i = 1; i<=n; i++){
        if(!deg[i]) q.push(i);
    }
    if(q.empty()){
        cout<<0;
        return 0;
    }
    while(!q.empty()){
        auto cur = q.front();
        q.pop();
        v.push_back(cur);
        for(int i = 0; i<adj[cur].size(); i++){
            deg[adj[cur][i]]--;
            if(!deg[adj[cur][i]]) {
                q.push(adj[cur][i]);
            }
        }
    }
    if(v.size() != n) {
        cout<<0;
        return 0;
    }
    for(int i = 0; i<v.size(); i++){
        cout<<v[i]<<'\n';
    }
}