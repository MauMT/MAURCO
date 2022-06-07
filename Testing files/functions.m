program Functions;


vars
{
    int i;
    float valor, y;
    char msg;
    int x;
    int arr[4], f, vector[10];
    int mat[2][3];
    int a, b, size, aux, marco;
}

int func factorialRecursivo(int n)
vars 
int aux, aux2;
{
  
  if (n < 1) then{
    aux = 1;
  } else{
    aux2 = n-1;
    aux = n * factorialRecursivo(aux2);
  }
  return(aux);
}

int func factorialIterativo(int n)
vars
int aux;
{
    aux = 1;
    while (n > 0) do {
        aux = aux * n;
        n = n - 1;
    }
    return(aux);
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


int func fibonacciIterativo(int n)
vars 
int aux, numAnterior, numAntesAnterior, numActual;
{
  numAnterior = 0;
  numAntesAnterior = 0;
  numActual = 1;
  while (n > 1) do{
    numAntesAnterior = numAnterior;
    numAnterior = numActual;
    numActual = numAntesAnterior + numAnterior;
    n = n - 1;
  }
  return(numActual);

}

int func mau(int n)
vars
int aux;
{
    aux = fibonacciIterativo(n);
    return(aux);
}


main(){
size = 99;
print(size);
x = 1;
print("a",size/x);


print("mau(10)", mau(10));
print("--------------------");
print("fibonacciRecursivo(10)", fibonacciRecursivo(10));
print("fibonacciIterativo(10)", fibonacciIterativo(10));
print("--------------------");
print("factorialRecursivo(5)", factorialRecursivo(5));
print("factorialIterativo(5)", factorialIterativo(5));
  

  


}
end