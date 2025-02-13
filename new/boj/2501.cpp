#include<bits/stdc++.h>
using namespace std;

int main()
{
    int N, K, idx = 0;
    int arr[10000];
    cin >> N >> K;
    for (int i = 1; i <= N; i++) {
        if (N % i == 0) {
            arr[idx] = i;
            idx += 1;
        }
    }
    if (idx + 1 < K) {
        cout << 0;
    } else {
    cout << arr[K-1];
    }

    return 0;
}
