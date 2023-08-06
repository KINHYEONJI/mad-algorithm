#include <iostream>

using namespace std;

int main(void)
{
    int hour, minute, time;
    cin >> hour >> minute >> time;

    cout << (hour + (minute + time) / 60) % 24 << " " << (minute + time) % 60;
}