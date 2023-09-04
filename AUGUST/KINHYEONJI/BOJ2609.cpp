#include <iostream>

using namespace std;

int main(void)
{
    int a, b;
    cin >> a >> b;
    int gcm, lcm;
    for (int i = 1; i < min(a, b) + 1; i++)
    {
        if (a % i == 0 && b % i == 0)
            gcm = i;
    }

    for (int i = min(a, b); i < a * b + 1; i++)
    {
        if (i % a == 0 && i % b == 0)
        {
            lcm = i;
            break;
        }
    }

    cout << gcm << "\n"
         << lcm;
}