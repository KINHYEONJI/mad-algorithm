#include <iostream>
#include <vector>
#include <map>

using namespace std;


int main() {
    map<string, pair<int, int>> moveMap;
    moveMap["R"] = make_pair(0, 1);
    moveMap["L"] = make_pair(0, -1);
    moveMap["B"] = make_pair(-1, 0);
    moveMap["T"] = make_pair(1, 0);
    moveMap["RT"] = make_pair(1, 1);
    moveMap["LT"] = make_pair(1, -1);
    moveMap["RB"] = make_pair(-1, 1);
    moveMap["LB"] = make_pair(-1, -1);

    string king, rock;
    int n;
    cin >> king >> rock >> n;
    int king_y = king[0] - 'A', king_x = king[1] - '1';
    int rock_y = rock[0] - 'A', rock_x = rock[1] - '1';
    for (int i = 0; i < n; i++) {
        string command;
        cin >> command;
        auto move = moveMap[command];
        if (king_x + move.first < 0 || king_y + move.second < 0 ||
            king_x + move.first >= 8 || king_y + move.second >= 8)
            continue;
        king_x += move.first;
        king_y += move.second;
        if (king_x == rock_x && king_y == rock_y) {
            if (rock_x + move.first < 0 || rock_y + move.second < 0 ||
                rock_x + move.first >= 8 || rock_y + move.second >= 8) {
                king_x -= move.first;
                king_y -= move.second;
                continue;
            }
            rock_x += move.first;
            rock_y += move.second;
        }
    }
    cout << char(king_y + 'A') << king_x + 1 << endl;
    cout << char(rock_y + 'A') << rock_x + 1 << endl;
}