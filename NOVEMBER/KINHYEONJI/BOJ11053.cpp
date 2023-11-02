#include <iostream>
#include <algorithm>

using namespace std;

int dp[1002];
int arr[1002];
int n;
int max_len = 0;

int main(){
    cin >>n;
    for(int i = 1; i<=n; i++){
        cin>>arr[i];
    }
    for(int i = 1; i<= 1000; i++){
        dp[i] = 1;
    }
    for(int i = 1; i<= n; i++){
        for(int j = i+1; j<= n; j++){
            if(arr[i] < arr[j]){
                dp[j] = max(dp[i]+1, dp[j]);
            }
        }
        max_len = max(max_len, dp[i]);
    }
    cout<<max_len;
}