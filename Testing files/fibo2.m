program fibonacci2;

vars{
    int i;
    float valor, y;
    char msg;
    int x;
    int arr[4], f, vector[10];
    int mat[2][3];
    int a, b, size, aux, marco;
}

int func fibonacciRecursivo(int n)
vars
int aux, aux2, aux3;
float x;
{
    if (n < 3) then{
        aux = 1;
        
    } else{
      aux2 = fibonacciRecursivo(n-1);
      aux3 = fibonacciRecursivo(n-2);
      aux = aux2 + aux3;
    }
    
    return(aux);
}


main(){

    print("--------------------");
    print("fibonacciRecursivo(10)", fibonacciRecursivo(20));
    print("--------------------");

}
end