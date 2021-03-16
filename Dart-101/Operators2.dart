// Relational and Logical Operators

void main() {
  // ==, !=, >, <, >=, <=
  var a = 10, b = 20;
  print(a < b); //true
  var c = a==b; 
  print(c); //false
  
  //!, &&, ||
  print((a == 10) && (b == 20));
  // true
  print((a > 10) || (b == 20));
  // true
  print(!(a==10) && (b==20));
  // false
}
