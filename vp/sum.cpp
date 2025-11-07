long double* liidetavad;
long double liida(int start, int end){
    if (end == start) return liidetavad[start];
    int keskkoht = (start + end) / 2;
    return (liida(start,keskkoht) + liida(keskkoht + 1, end));
}