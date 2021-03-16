/* Well, you know the drill.Let's Do it again.*/

void main() {
  var x = 0,y = 0;
  while(x < 5){
    print(x);
    x++;
  }
  //0 1 2 3 4
  do{
    print(y);
  } while(y != 0);
  //0
  
  /* break and continue */
  for(var x = 0;x < 5;x++){
    if(x == 0) continue;
    else if(x == 4) break;
    else print(x);
  }
  // 1 2 3
}