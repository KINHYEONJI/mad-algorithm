#include <iostream>
#include <algorithm>
#include <stack>

using namespace std;
int dp[1002][1002];

int main(){
    string str1, str2;
    cin>>str1>>str2;
    for(int i = 0; i<str1.size(); i++){
        for(int j = 0; j<str2.size(); j++){
            if(str1[i] == str2[j]){
                dp[i+1][j+1] = dp[i][j] + 1;
            }
            else{
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j]);
            }
        }
    }
    cout<<dp[str1.size()][str2.size()]<<'\n';
    int x = str1.size();
    int y = str2.size();
    stack<char> max_str;
    while(x>0 && y>0){
        if(dp[x-1][y] == dp[x][y]){
            x--;
            continue;
        }
        else if (dp[x][y-1] == dp[x][y]){
            y--;
            continue;
        }
        if(dp[x-1][y-1] == dp[x][y]-1){
            max_str.push(str1[x-1]);
            x--;
            y--;
            continue;
        }
    }
    while(!max_str.empty()){
        cout<<max_str.top();
        max_str.pop();
    }
}