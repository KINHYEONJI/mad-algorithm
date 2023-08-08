#include <iostream>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

int main()
{
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;

    while (T--)
    {
        string buffer;
        getline(cin, buffer);
        string origin;
        getline(cin, origin);

        map<string, bool> m;
        while (true)
        {
            string animal, goes, sound;
            cin >> animal >> goes >> sound;
            if (animal == "what")
                break;
            m[sound] = true;
        }

        string res = "";
        for (int i = 0; i < origin.size(); i++)
        {
            if (origin[i] == ' ')
            {
                if (!m[res])
                {
                    cout << res << " ";
                }
                res = "";
            }
            else
                res += origin[i];
        }
        if (!m[res])
        {
            cout << res << " ";
        }
        cout << '\n';
    }
}
