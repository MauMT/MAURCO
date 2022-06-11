program SortFindVector;

vars
{
    int i, j;
    float valor, y;
    char msg;
    int x;
    int arr[4], f, vector[10];
    int mat[2][3];
    int a, b, size, aux, mau;
}


main(){
  mau = 1;
  i = 0;
  f = 17;
  vector[0] = 19;
  vector[1] = 27;
  vector[2] = 7;
  vector[3] = 27;
  vector[4] = 29;
  vector[5] = 17;
  vector[6] = 18;
  vector[7] = 16;
  vector[8] = 28;
  vector[9] = 14;

  while (i<10) do{
    if(vector[i] == f) then {
      print("True");
    }
    i = i + 1;
  }

print("------");
a = 0;
b = 0;
size = 10;
  
while (a < (size-1)) do {
  while (b < (size-a-1)) do {
    
    if(vector[b] > vector[b+1]) then {
        aux = vector[b];
        vector[b] = vector[b+1];
        vector[b+1] = aux;
    }
    b = b + 1;
  }
  a = a + 1;
  b = 0;
}

mat[0][0] = 1;
mat[0][1] = 2;
mat[0][2] = 3;
mat[1][0] = 4;
mat[1][1] = 5;
mat[1][2] = 6;


i=0;
j=0;
f = 8;

while (i<2) do{
    
    while(j<3) do{
    if(mat[i][j] == f) then {
      print("True");
    }
    j = j+1;
  }
  j=0;
  i = i + 1;
}

i = 0;
while(i< 10) do{
  print(vector[i]);
  i = i + 1;
}

y=17.3;
valor = 7.3;

if(y-valor==11) then{
  print("Verdadero");
} else{
  print("Falso");
}

input(y);
print(y);
  
  


}
end