#include<iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
ll D = 1000000007;
int main(){
  	int N, M;
  	cin >> N >> M;
    bool safe[N+1];
    for(int i=0;i<=N;i++) safe[i] = true;

    for(int i=0;i<M;i++){
        int a;
        cin >> a;
        safe[a] = false;
    }

    ll pat[N+1];
    pat[0] = 1;
    if(safe[1]){
        pat[1] = 1;
    }else{
        pat[1] = 0;
    }

    for(int i=2;i<=N;i++){
        if(safe[i]){
            pat[i] = pat[i-1] + pat[i-2];
            pat[i] = pat[i]%D;
        }else{
            pat[i] = 0;
        }
    }
    cout << pat[N] <<endl;


  	return 0;
}
