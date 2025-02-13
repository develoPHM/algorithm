#include<bits/stdc++.h>
using namespace std;

int main()
{
    int N, cnt, ans = 0;
    cin >> N;
    vector<int> arr(N);

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }
    for (int i = 0; i < N; i++) {
        cnt = 0;
        for (int j = 1; j < arr[i] + 1; j++) {
            if (arr[i] == 1) {
                continue;
            }
            if (arr[i] % j == 0) {
                cnt = cnt + 1;
            }
        }
        if (cnt == 2) {
            ans += 1;
        }
    }
    cout << ans;
}