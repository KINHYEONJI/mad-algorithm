#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    vector<string> str_arr;
    for (int i = 0; i < n; i++)
    {
        string str;
        cin >> str;
        str_arr.push_back(str);
    }

    string answer = "";
    int hamming_d = 0;
    char acgt[5] = "ACGT";

    for (int i = 0; i < m; i++)
    {
        int count_acgt[4] = {0};
        for (int j = 0; j < n; j++)
        {
            if (str_arr[j][i] == 'A')
                count_acgt[0]++;
            else if (str_arr[j][i] == 'C')
                count_acgt[1]++;
            else if (str_arr[j][i] == 'G')
                count_acgt[2]++;
            else if (str_arr[j][i] == 'T')
                count_acgt[3]++;
        }
        int *max_count = max_element(count_acgt, count_acgt + 4);
        int max_index = distance(count_acgt, max_count);
        answer += acgt[max_index];
        hamming_d += (n - *max_count);
    }
    cout << answer << '\n'
         << hamming_d;
    return 0;
}