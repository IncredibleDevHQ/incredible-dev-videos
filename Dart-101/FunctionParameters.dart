/* Sometimes you gotta give something 
   to some people to help em out! */

void named({int x : 0}){
  print(x);
}
//void named({int? x}){}

void namedRequired({required int x}){
  print(x);
}

void pos(int x, [int? y]){
  print("$x $y");
}

void main() {
  named(x : 10); //10
  namedRequired(x : 10); //10
  pos(10); //10 null
  pos(10,20);// 10 20
}