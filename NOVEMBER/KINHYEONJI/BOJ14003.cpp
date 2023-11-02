#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int n;
    cin>>n;
    vector<int> v(n);
    for(int i = 0; i<n; i++){
        cin>>v[i];
    }
    vector<int> increase_v;
    vector<int> record(n);
    increase_v.push_back(v[0]);
    record[0] = 1;
    for(int i = 1; i<n; i++){
        if(*(increase_v.end()-1) < v[i]){
            increase_v.push_back(v[i]);
            record[i] = increase_v.size();
        }
        else{
            int index = lower_bound(increase_v.begin(), increase_v.end(), v[i])-increase_v.begin();
            increase_v[index] = v[i];
            record[i] = index+1;
        }
    }
    int increase_v_size = increase_v.size();
    cout<<increase_v_size<<'\n';
    int find_i = increase_v_size;
    vector<int> v_num(increase_v_size);
    for(int i = n-1; i>= 0; i--){
        if(record[i] == find_i){
            v_num[find_i-1] = v[i];
            find_i--;
        }
    }
    for(int i = 0; i< increase_v_size; i++){
        cout<<v_num[i]<<" ";
    }
}