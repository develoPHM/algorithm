#include <bits/stdc++.h>
using namespace std;
int main() {
  vector<vector<string>> v(5, vector<string>(1));
  for (int i = 0; i < 5; ++i) {
    cin >> v[i][0];
  }

  for (int i = 0; i < 5; ++i) {
    cout << v[i][0] << endl;
  }
  cout << endl;
}