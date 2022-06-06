program Expresion;


vars
{
    int i;
    float valor, y;
    char msg;
    int x;
    int arr[4], f, vector[10];
    int mat[2][3];
    int a, b, size, aux;
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


main(){
  print("factorial recursivo de 5", factorialRecursivo(5));
  print("factorial iterativo de 5", factorialIterativo(5));

  print("fibonacci iterativo de 10 es", fibonacciIterativo(10));









  


}
end