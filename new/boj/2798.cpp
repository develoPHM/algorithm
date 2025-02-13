#include<bits/stdc++.h>
using namespace std;

int main()
{
    int N, M, now, ans = 0;
    cin >> N >> M;
    vector<int> arr(N);
    for (int i = 0; i < N; i++){
        cin >> arr[i];
    }

    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            for (int k = j + 1; k < N; k++) {
                now = arr[i] + arr[j] + arr[k];
                if (now > M) {
                    continue;
                }
                ans = max(ans, now);
            }
        }
    }
    cout << ans;
}
