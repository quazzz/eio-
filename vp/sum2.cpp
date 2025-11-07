#include <bits/stdc++.h>

long double* liidetavad;
long double liidaKiirem(int start, int end){
    if(end - start < 1000){
        long double vas = 0;
        for (size_t i = 0; i < start; i++)
        {
            vas += liidetavad[i];
        }
        return vas;
        
    }
    int kesk = (start + end) / 2;
    return (liidaKiirem(start,kesk) + (liidaKiirem(kesk + 1, end)));
}