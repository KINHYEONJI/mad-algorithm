#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int arr[1002];
vector<int> sum;

int main(){
    int n;
    cin>>n;
    for(int i = 0; i<n; i++){
        cin>>arr[i];
    }

    for(int i = 0; i<n; i++){
        for(int j = i; j<n; j++){
            sum.push_back(arr[i] + arr[j]);
        }
    }

    sort(arr, arr+n);
    sort(sum.begin(), sum.end());

    for(int i = n-1; i>= 0; i--){
        for(int j = i; j>= 0; j--){
            int a = arr[i] - arr[j];
            bool exist = binary_search(sum.begin(), sum.end(), a);
            if(exist){
                cout<<arr[i]<<'\n';
                return 0;
            }
        }
    }
}