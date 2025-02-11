#include<bits/stdc++.h>
using namespace std;

int main()
{
    while (true) {
        int a, b;
        cin >> a >> b;
        if (a == 0 and b == 0) {
            break;
        }
        if (a > b and a % b == 0) {
            cout << "multiple";
        } else if (a < b and b % a == 0) {
            cout << "factor";
        } else {
            cout << "neither";
        }
        cout << endl;
    }

    return 0;
}

