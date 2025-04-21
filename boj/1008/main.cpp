#include <bits/stdc++.h>
using namespace std;

int main() {
    double A, B;
    cin >> A >> B;

    // 🔥 소수점 15자리까지 출력
    cout << fixed << setprecision(15) << A / B;

    return 0;
}