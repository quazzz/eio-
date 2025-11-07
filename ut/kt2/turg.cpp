#include <vector>
#include <cmath>
#include <iostream>

using namespace std;
int binSearch(const vector<int>& hinnad, int soov){
    int N = hinnad.size();
    int low = 0, high = N - 1;
    while(low < high) {
        int mid = (low + high) / 2;
        if(hinnad[mid] < soov){
            low = mid + 1;
        }
        else {
            high = mid;
        }
    }
    return low;
}
int main()
{
   
    int N,M; cin >> N >> M;
    vector<int> hinnad(N);
    vector<int> vastus;
    for (size_t i = 0; i < N; i++)
    {
        int temp; cin >> temp;
        hinnad[i] = temp;
    }
    vector<int> soovitud(M);
    for (size_t i = 0; i < M; i++)
    {
        int temp; cin >> temp;
        soovitud[i] = temp;
    }
    for (size_t i = 0; i < M; i++)
    {
        int indeks = binSearch(hinnad, soovitud[i]);
        int valik;
        if(indeks == 0){
            vastus.push_back(hinnad[0]);
        }
        else if(indeks >= N){
            vastus.push_back(hinnad[N - 1]);
        }
        else{
            int vahe1 = abs(hinnad[indeks] - soovitud[i]);
            int vahe2= abs(hinnad[indeks - 1] - soovitud[i]);
            if(vahe1 < vahe2){
                vastus.push_back(hinnad[indeks]);
            }
            else{
                vastus.push_back(hinnad[indeks - 1]);
            }
        }

    }
    for (size_t i = 0; i < M; i++)
    {   
        if(i == M - 1){
            cout << vastus[i];
        }
        else{
           cout << vastus[i] << ' '; 
        }
        
    }
    
    
    
    

    
    return 0;
}