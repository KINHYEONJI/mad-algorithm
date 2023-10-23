#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>

using namespace std;

int n;
int parent[1002];

int find_(int x){
    if(parent[x] == x) return x;
    return parent[x] = find_(parent[x]);
}

bool union_(int a, int b){
    a = find_(a);
    b = find_(b);
    if(a==b) return false;
    else{
        parent[b] = a;
        return true;
    }
}



int main(){
    cin>>n;
    vector<tuple<int, int, int>> v;
    for(int i = 1; i<=n; i++){
        parent[i] = i;
    }
    for(int i = 1; i<=n; i++){
        for(int j = 1; j<=n; j++){
            int w;
            cin>>w;
            if(i==j) continue;
            v.push_back({w, i ,j});
        }
    }
    sort(v.begin(), v.end());

    int w, s, e;
    long long answer = 0;
    for(auto vv : v){
        tie(w, s, e) = vv;
        if(union_(s, e)){
            answer += w;
        }
    }
    cout<<answer;
}