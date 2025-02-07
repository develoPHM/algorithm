#include<bits/stdc++.h>
using namespace std;

int main() {
  int A, B;
  cin >> A >> B;

  vector<vector<int> > v1(A, vector<int>(B));
  vector<vector<int> > v2(A, vector<int>(B));
  vector<vector<int> > v(A, vector<int>(B));

  for (int i = 0; i < A; ++i) {
    for (int j = 0; j < B; ++j) {
      cin >> v1[i][j];
    }
  }

  for (int i = 0; i < A; ++i) {
    for (int j = 0; j < B; ++j) {
      cin >> v2[i][j];
    }
  }

  for (int i = 0; i < A; ++i) {
    for (int j = 0; j < B; ++j) {
      v[i][j] = v1[i][j] + v2[i][j];
    }
  }


  for (int i = 0; i < A; ++i) {
    for (int j = 0; j < B; ++j) {
      cout << v[i][j] << ' ';
    }
    cout << endl;
  }

  return 0;
}