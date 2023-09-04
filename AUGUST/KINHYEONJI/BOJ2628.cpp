#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> row;
    vector<int> column;
    int num;
    cin >> num;
    row.push_back(0);
    column.push_back(0);
    for (int i = 0; i < num; i++) {
        int x, y;
        cin >> x >> y;
        if (x == 1)
            row.push_back(y);
        else column.push_back(y);
    }
    sort(row.begin(), row.end());
    sort(column.begin(), column.end());
    row.push_back(n);
    column.push_back(m);

    int max_row = 0;
    int max_column = 0;
    for (int i = 0; i < row.size() - 1; i++) {
        max_row = max(max_row, row[i + 1] - row[i]);
    }
    for (int i = 0; i < column.size() - 1; i++) {
        max_column = max(max_column, column[i + 1] - column[i]);
    }

    cout << max_row * max_column;
}