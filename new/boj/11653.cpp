#include<bits/stdc++.h>
using namespace std;

int main()
{
    int N;
    cin >> N;
    while (true) {
        if (N == 1) {
            break;
        }
        for (int i = 2; i <= N; i++) {
            if (N % i == 0) {
                N = N / i;
                cout << i;
                break;
            }
        }
        cout << endl;
    }

    return 0;
}