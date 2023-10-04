#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int g, p;
    cin >> g >> p;

    vector<int> memory(100001, 0);
    vector<int> gate(100001, 0);
    int answer = 0;
    for(int i = 0; i<p; i++){
        int n;
        int flag = 0;
        cin>>n;
        if(memory[n]){
            for(int j = memory[n]; j>0; j--){
                if(!gate[j]){
                    gate[j] = n;
                    memory[n]= j;
                    flag = 1;
                    answer++;
                    break;
                }
            }
        }
        else{
            for(int j = n; j>0; j--){
                if(!gate[j]){
                    gate[j] = n;
                    memory[n] = j;
                    flag = 1;
                    answer++;
                    break;
                }
            }
        }
        if(!flag) break;
    }
    cout<<answer;
}