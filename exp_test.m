program Expresion;


vars
{
    int i;
    float valor, y;
    char msg;
    int x;
    int arr[4], f;
    int mat[2][3], aux, n;
}



main(){
    
    
    i=0;
    x = 5;
    while(i<3) do {
      print(i);
      arr[i] = 888;
      i = i+1;
    }


aux = 1;
  n=5;
  while (n>0) do {
    aux = aux*n;
    n = n-1;
  }
  print(aux);

}
end