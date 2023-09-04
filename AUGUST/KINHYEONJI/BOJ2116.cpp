#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<vector<int>> dice_arr;
    for (int i = 0; i < n; i++) {
        vector<int> dice;
        for (int j = 0; j < 6; j++) {
            int num;
            cin >> num;
            dice.push_back(num);
        }
        dice_arr.push_back(dice);
    }
    int pair[6] = {5, 3, 4, 1, 2, 0};

    int max_sum = 0;
    for (int i = 0; i < 6; i++) {
        vector<vector<int>> dice_side_arr;
        int contact_value = dice_arr[0][i];
        for (int j = 0; j < n; j++) {
            vector<int> side_arr = {1, 2, 3, 4, 5, 6};
            for (int k = 0; k < 6; k++) {
                if (dice_arr[j][k] == contact_value) {
                    side_arr.erase(remove(side_arr.begin(), side_arr.end(), contact_value));
                    side_arr.erase(remove(side_arr.begin(), side_arr.end(), dice_arr[j][pair[k]]));
                    contact_value = dice_arr[j][pair[k]];
                    break;
                }
            }
            dice_side_arr.push_back(side_arr);
        }
        int sum_ = 0;
        for (int j = 0; j < n; j++) {
            sum_ += dice_side_arr[j][3];
        }
        max_sum = max(max_sum, sum_);
    }
    cout << max_sum;


}