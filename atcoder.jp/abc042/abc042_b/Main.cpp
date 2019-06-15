#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
    int N,L;
    vector<string> a;
    cin >> N >> L;
    for(int i=0; i<N; i++){
        string s;
        cin >> s;
        a.push_back(s);
    }
    sort(a.begin(),a.end());
    string s = "";
    for(int i=0; i<N; i++){
        s += a[i];
    }
    cout << s << endl;
    return 0;
}