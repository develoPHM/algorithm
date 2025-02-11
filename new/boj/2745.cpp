// #include<bits/stdc++.h>
// using namespace std;
//
// int convert(const char c)
// {
//     if ('A' <= c && c <= 'Z')
//     {
//         return c - 'A' + 10;
//     }
//     return c - '0';
// }
//
// int main()
// {
//     string N;
//     int ans = 0, w = 1, B;
//     cin >> N >> B;
//
//     for (int i = 0; i < N.size(); ++i)
//     {
//         ans += convert(N[N.size() - i - 1]) * w;
//         w = w * B;
//     }
//
//     cout << ans;
//     return 0;
// }
#include<bits/stdc++.h>
using namespace std;
int main()
{
    string a = "2";
    cout << stoi(a);
}