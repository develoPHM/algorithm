#include<bits/stdc++.h>
using namespace std;

int main() {
    vector<vector<int> > v(9, vector<int>(9, 0));
    int max_num = -1, r = 0, w = 0;
    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) {
            cin >> v[i][j];
            if (v[i][j] > max_num) {
                max_num = v[i][j];
                r = i;
                w = j;
            }
        }
    }
    cout << max_num << endl;
    cout << r + 1 << ' ' << w + 1;
}
