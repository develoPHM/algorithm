#include<bits/stdc++.h>
using namespace std;
int main()
{
    int num, check, ans = 1000001;
    string n;
    cin >> num;
    check = num;
    while (num > 0) {
        int sum_num = 0;
        n = to_string(num);
        for (char c : n) {
            sum_num += c - '0';
        }
        sum_num += num;
        if (sum_num == check) {
            ans = min(num, ans);
        }
        num -= 1;
    }
    if (ans == 1000001) {
        cout << 0;
    } else
    cout << ans;
}