#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int home_x, home_y, fest_x, fest_y;
        cin >> home_x >> home_y;
        vector<pair<int, int>> con_v;
        vector<int> visited(n, 0);
        while(n--){
            int con_x, con_y;
            cin>>con_x>>con_y;
            con_v.push_back({con_x, con_y});
        }
        cin >> fest_x >> fest_y;
        queue<pair<int, int>> q;
        int is_happy = 0;
        q.push({home_x, home_y});
        while(!q.empty()){
            auto cur = q.front();
            q.pop();
            for(int i = 0; i<n; i++){
                if(abs(con_v[i].first - cur.first) + abs(con_v[i].second - cur.second) <= 1000){
                    if(!visited[i]){
                        visited[i] = 1;
                        q.push(con_v[i]);
                    }
                }
            }
            if(abs(fest_x - cur.first) + abs(fest_y - cur.second) <= 1000){
                is_happy = 1;
                break;
            }
        }
        is_happy ? cout<<"happy\n" : cout<<"sad\n";
    }
}