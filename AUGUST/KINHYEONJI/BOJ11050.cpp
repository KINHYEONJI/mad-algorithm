#include <iostream>

using namespace std;

int main(void)
{
    int a, b;
    cin >> a >> b;
    int mom = 1, son = 1;
    for (int i = 0; i < b; i++)
    {
        mom *= a--;
    }
    for (int i = b; i > 0; i--)
    {
        son *= i;
    }
    cout << mom / son;
}