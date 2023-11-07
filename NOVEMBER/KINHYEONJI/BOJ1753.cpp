#include <iostream>
#include <queue>
#include <vector>

#define x first
#define y second

using namespace std;

int V, E, st;
vector<pair<int, int>> adj[20'002];
int d[20'002] = {0};
int INF = 0x3f3f3f3f;

int main(){
    cin>>V>>E>>st;
    fill(d, d+V+1, INF);
    while(E--){
        int u, v, w;
        cin>>u>>v>>w;
        adj[u].push_back({w, v});
    }
    d[st] = 0;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
    pq.push({0, st});
    while(!pq.empty()){
        auto cur = pq.top();
        pq.pop();
        if(d[cur.y] != cur.x) continue;
        for(auto nxt : adj[cur.y]){
            if(d[nxt.y] > d[cur.y] + nxt.x){
                d[nxt.y] = d[cur.y] + nxt.x;
                pq.push({d[nxt.y], nxt.y});
            }
        }
    }
    for(int i = 1; i <= V; i++){
        if(d[i] == INF) cout << "INF\n";
        else cout << d[i] << "\n";
    }
}