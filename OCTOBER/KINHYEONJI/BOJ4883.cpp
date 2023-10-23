#include <iostream>
#include <algorithm>

using namespace std;
int arr[100002][3];
int dp[100002][3];
int dx[] = {0, 1, 1, 1};
int dy[] = {1, -1, 0, 1};

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t = 1;
    while(true){
        int n;
        cin>>n;
        if(n== 0) break;
        for(int i = 0; i<n; i++){
            for(int j = 0; j<3; j++){
                cin>>arr[i][j];
            }
        }

        for(int i = 0; i<n; i++){
            fill(dp[i], dp[i] + 3, 0x3f3f3f3f);
        }

        dp[0][1] = arr[0][1];

        for(int i = 0; i<n; i++){
            for(int j = 0; j<3; j++){
                if(i==0 && j == 0) continue;
                for(int dir = 0; dir<4; dir++){
                    int nx = i + dx[dir];
                    int ny = j + dy[dir];
                    if(nx <0 || ny<0 || nx >= n || ny >= 3) continue;
                    dp[nx][ny] = min(dp[nx][ny], dp[i][j] + arr[nx][ny]);
                }
            }
        }
        cout<<t<<". "<<dp[n-1][1]<<'\n';
        t++;
    }
}