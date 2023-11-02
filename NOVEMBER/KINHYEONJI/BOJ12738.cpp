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
    increase_v.push_back(v[0]);
    for(int i = 1; i<n; i++){
        if(*(increase_v.end()-1) < v[i]){
            increase_v.push_back(v[i]);
        }
        else{
            increase_v[lower_bound(increase_v.begin(), increase_v.end(), v[i])-increase_v.begin()] = v[i];
        }
    }
    cout<<increase_v.size();
}