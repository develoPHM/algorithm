#include<bits/stdc++.h>
using namespace std;

int main()
{
    int a, b, c, d, e, f;
    cin >> a >> b >> c >> d >> e >> f;

    for (int i = -999; i <= 999; i++) {
        for (int j = -999; j <= 999; j++) {
            if ((i * a + j * b == c) and (i * d + j * e == f)) {
                cout << i << " " << j;
                return 0;
            }
        }
    }
}
