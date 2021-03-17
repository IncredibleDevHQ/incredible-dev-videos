/* Too much for one person to handle? */
/* Divide responsibilities ;) */

void show(){
  print("Hello Incredibles!");
}
// void show() => print("");

int add(int x,int y){
  return x+y;
}

void main() {
  show();
  var result = add(2,3);
  print(result); //5
  //print(result(2,3));
}