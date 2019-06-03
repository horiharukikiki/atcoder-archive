#include<iostream>
using namespace std;
#include<vector>

int main(){
  int N,M,X,Y;
  cin>>N>>M>>X>>Y;
  vector <int> AB(N);
  vector <int> BA(M);
  for(int i=0;i<N;i++)
    cin>>AB[i];
  for(int i=0;i<M;i++)
    cin>>BA[i];

  int now=0;
  int i=0,j=0;
  int count=0;

  while(i<N){
    if(AB[i]>=now){
      now=AB[i]+X;
      i++;
      while(j<M){
        if(BA[j]>=now){
          now=BA[j]+Y;
          count++;
          j++;
          break;
        }else{
          j++;
        }
      }
    }
    else{
      i++;
    }
  }

  cout<<count<<endl;
}
