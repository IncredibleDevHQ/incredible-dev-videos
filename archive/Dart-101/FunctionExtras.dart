/* Some functions be like "I am no one" */
/* And other such quirks :P */

void main() {
  var list = [1, 2, 3, 4, 5];
  
  // (paramenter) { codeBlock }
  list.forEach(
    (num) { print(num); }
  );
  
  // function inside function
  // Lexical scope and closure
  Function makeAdder(int addBy) {
    return (int i) => addBy + i;
  }
  
  var add2 = makeAdder(2);
  print(add2(3)); //5
}
