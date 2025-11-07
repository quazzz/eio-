bool onAlgarv(int a){
    for(int i = 2; i< a; ++i){
        if(a % i == 0){
            return false;
        }
    }
    return true;
}
bool onAlgarv2(int a){
    if(a % 2 == 0){
        return false;
    }
    for(int i = 0; i < 3; i+=2){
        if(a % i == 0){
            return false;
        }
    }
    return true;
}
bool onAlgarv3(int a){
    if(a % 2 == 0) return false;
    for(int i = 3; i * i<= a; i+=2){
        if(a % i == 0) return false;
    }
    return true;
}