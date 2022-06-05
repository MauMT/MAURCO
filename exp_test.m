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


main(){

  i=7;
  vector[0] = 1;
  vector[1] = 9;
  vector[2] = 11;
  vector[3] = 7;
  vector[4] = 15;
  vector[5] = 17;
  vector[6] = 21;
  vector[7] = 21;
  vector[8] = 20;
  vector[9] = 25;


  


a = 0;
b = 0;
size = 10;
  
  while (a < size) do {
    while (b < size-a-1) do {
      if(vector[b] > vector[b+1]) then {
        aux = vector[b];
        vector[b] = vector[b+1];
        vector[b+1] = aux;
        b = b + 1;
    }
    a = a + 1;
  }
  i = 0;

  while(i< 10) do{
    print(vector[i]);
    i = i + 1;
  }



  


}
end