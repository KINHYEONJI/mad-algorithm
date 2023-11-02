#include <iostream>
#include <algorithm>

using namespace std;

int n;
int dp[1002];
int arr[1002];

int main(){
    cin>>n;
    for(int i = 0; i<n; i++){
        cin>>arr[i];
        dp[i] = arr[i];
    }

    int max_sum = 0;
    for(int i = 0; i<n; i++){
        for(int j = i+1; j<n; j++){
            if(arr[i]<arr[j]){
                dp[j] = max(dp[i]+ arr[j], dp[j]);
            }
        }
        max_sum = max(max_sum, dp[i]);
    }
    cout<<max_sum;
}