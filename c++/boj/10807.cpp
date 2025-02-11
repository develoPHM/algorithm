#include<bits/stdc++.h>
using namespace std;

int main()
{
    int N;
    // N 초기화
    cin >> N;

    // 배열에 값 넣기
    int v[N];

    // for (int i = 0; i < N; ++i) {
    //   cin >> arr[i];
    // }
    for (int i = 0; i < N; ++i)
    {
        cout << v[i] << ' ';
    }

    cout << endl;
    cout << typeid(v).name();

    //
    //    // V 초기화
    //    cin >> V;
    //
    //    for (int i =0; i < N; ++i) {
    //      if (arr[i] == V) {
    //        cnt += 1;
    //      }
    //    }
    //
    //    // cnt 출력
    //    cout << cnt;
    //
    return 0;
}
