#include <bits/stdc++.h>
using namespace std;

int arr[100005];
int n;
int state[100005];

void run(int x){
    int cur = x;
    while(true){
        state[cur] = x;
        cur = arr[cur];
        if(state[cur] == x){
            while(state[cur] != -1){
                state[cur] = -1;
                cur = arr[cur];
            }
            return;
        }
        else if(state[cur] != 0) return;
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    while(t--){
        cin >> n;
        fill(state+1, state+n+1, 0);
        for(int i = 1; i <= n; i++)
            cin >> arr[i];
        for(int i = 1; i <= n; i++){
            if(state[i] == 0) run(i);
        }
        int cnt = 0;
        for(int i = 1; i <= n; i++){
            if(state[i] != -1) cnt++;
        }
        cout << cnt << '\n';
    }
}