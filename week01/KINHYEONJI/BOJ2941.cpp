#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    string findArr[] = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
    int alphabetLen[] = {1, 1, 2, 1, 2, 2, 1, 1};

    string str;
    cin >> str;

    int count = 0;
    int n = 0;
    for (int i = 0; i < 8; i++)
    {
        int f = str.find(findArr[i]);
        while (f != string::npos)
        {
            count += alphabetLen[i];
            str = str.replace(f, findArr[i].size(), "1");
            f = str.find(findArr[i]);
            n += alphabetLen[i];
        }
    }
    cout << count + str.size() - n;
}