program fibonacci1;

vars{
    int i;
    float valor, y;
    char msg;
    int x;
    int arr[4], f, vector[10];
    int mat[2][3];
    int a, b, size, aux, marco;
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

    print("--------------------");
    print("fibonacciIterativo(10)", fibonacciIterativo(10));
    print("--------------------");


}
end